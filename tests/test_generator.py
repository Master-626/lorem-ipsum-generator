import pytest

from lorem_generator.generator import LOREM_WORDS, LoremGenerator


def test_vocabulary_is_plain_lowercase_words():
    assert LOREM_WORDS
    assert len(LOREM_WORDS) == len(set(LOREM_WORDS))
    for word in LOREM_WORDS:
        assert word.isalpha()
        assert word.islower()


def test_generate_words():
    gen = LoremGenerator(seed=42)
    words = gen.generate_words(10)
    assert words.split() == [
        "esse",
        "elit",
        "ipsum",
        "cupidatat",
        "magna",
        "et",
        "labore",
        "sed",
        "cupidatat",
        "adipiscing",
    ]
    assert all(word in LOREM_WORDS for word in words.split())


def test_generate_words_zero_and_negative():
    gen = LoremGenerator(seed=1)
    assert gen.generate_words(0) == ""
    with pytest.raises(ValueError, match="count must be non-negative"):
        gen.generate_words(-1)
    with pytest.raises(TypeError, match="count must be an int"):
        gen.generate_words(1.5)


def test_generate_sentence():
    gen = LoremGenerator(seed=42)
    sentence = gen.generate_sentence()
    assert sentence == (
        "Ipsum cupidatat magna et labore sed cupidatat adipiscing pariatur."
    )
    assert sentence.endswith(".")
    assert sentence[0].isupper()
    assert sentence.count(".") == 1


def test_generate_sentence_word_bounds():
    for seed in range(20):
        sentence = LoremGenerator(seed=seed).generate_sentence(min_words=4, max_words=6)
        words = sentence[:-1].split()
        assert 4 <= len(words) <= 6
        assert sentence.endswith(".")
        assert words[0][0].isupper()


def test_start_with_lorem_keeps_requested_length():
    sentence = LoremGenerator(seed=1).generate_sentence(
        min_words=3, max_words=3, start_with_lorem=True
    )
    assert sentence == "Lorem ipsum dolor."

    short = LoremGenerator(seed=1).generate_sentence(
        min_words=1, max_words=1, start_with_lorem=True
    )
    assert short == "Lorem."

    classic = LoremGenerator(seed=42).generate_sentence(start_with_lorem=True)
    assert classic == (
        "Lorem ipsum dolor sit amet sed cupidatat adipiscing pariatur."
    )
    assert classic.lower().startswith("lorem ipsum dolor sit amet")


def test_sentence_bounds_are_validated():
    gen = LoremGenerator(seed=1)
    with pytest.raises(ValueError, match="cannot be greater than"):
        gen.generate_sentence(min_words=9, max_words=2)
    with pytest.raises(ValueError, match="min_words must be at least 1"):
        gen.generate_sentence(min_words=0, max_words=0)
    with pytest.raises(TypeError):
        gen.generate_sentence(min_words=1.2, max_words=4)


def test_generate_paragraph():
    paragraph = LoremGenerator(seed=42).generate_paragraph()
    assert paragraph == (
        "Cupidatat magna et labore sed cupidatat adipiscing pariatur. "
        "In laboris dolor ipsum consectetur ut labore commodo reprehenderit. "
        "Aute incididunt sint cillum excepteur duis ullamco labore."
    )
    assert paragraph.count(".") == 3


def test_generate_paragraph_sentence_bounds():
    paragraph = LoremGenerator(seed=3).generate_paragraph(
        min_sentences=2, max_sentences=2
    )
    assert paragraph.count(".") == 2
    gen = LoremGenerator(seed=1)
    with pytest.raises(ValueError, match="cannot be greater than"):
        gen.generate_paragraph(min_sentences=4, max_sentences=1)
    with pytest.raises(ValueError, match="min_sentences must be at least 1"):
        gen.generate_paragraph(min_sentences=0, max_sentences=0)


def test_generate_paragraphs():
    paragraphs = LoremGenerator(seed=42).generate_paragraphs(2)
    blocks = paragraphs.split("\n\n")
    assert len(blocks) == 2
    assert blocks[0].startswith("Cupidatat magna")
    assert LoremGenerator(seed=1).generate_paragraphs(0) == ""
    with pytest.raises(ValueError):
        LoremGenerator(seed=1).generate_paragraphs(-2)


def test_generate_html_paragraphs():
    html = LoremGenerator(seed=42).generate_html_paragraphs(2)
    assert html.count("<p>") == 2
    assert html.count("</p>") == 2
    assert "<p>Cupidatat magna" in html
    assert LoremGenerator(seed=1).generate_html_paragraphs(0) == ""
    with pytest.raises(ValueError):
        LoremGenerator(seed=1).generate_html_paragraphs(-1)


def test_generate_list():
    unordered = LoremGenerator(seed=42).generate_list(3)
    ordered = LoremGenerator(seed=42).generate_list(3, ordered=True)
    assert unordered == (
        "<ul>\n"
        "  <li>esse elit ipsum cupidatat magna</li>\n"
        "  <li>et labore sed cupidatat adipiscing</li>\n"
        "  <li>pariatur cupidatat id duis consectetur</li>\n"
        "</ul>"
    )
    assert ordered.startswith("<ol>\n")
    assert ordered.endswith("</ol>")
    assert unordered.count("<li>") == ordered.count("<li>") == 3
    assert LoremGenerator(seed=1).generate_list(0) == "<ul></ul>"
    assert LoremGenerator(seed=1).generate_list(0, ordered=True) == "<ol></ol>"
    with pytest.raises(ValueError):
        LoremGenerator(seed=1).generate_list(-1)


def test_generate_chars_exact_length_and_vocabulary():
    text = LoremGenerator(seed=42).generate_chars(11)
    assert text == "esse elit i"
    longer = LoremGenerator(seed=42).generate_chars(80)
    assert len(longer) == 80
    assert longer.startswith("esse elit ipsum")
    assert "  " not in longer
    parts = longer.split(" ")
    for part in parts[:-1]:
        assert part in LOREM_WORDS
    assert any(word.startswith(parts[-1]) for word in LOREM_WORDS)


def test_generate_chars_edges():
    assert LoremGenerator(seed=1).generate_chars(0) == ""
    one = LoremGenerator(seed=42).generate_chars(1)
    assert one == "e"
    with pytest.raises(ValueError, match="count must be non-negative"):
        LoremGenerator(seed=1).generate_chars(-5)
    with pytest.raises(TypeError, match="count must be an int"):
        LoremGenerator(seed=1).generate_chars("80")


def test_seed_reproducibility():
    methods = (
        lambda gen: gen.generate_words(5),
        lambda gen: gen.generate_chars(40),
        lambda gen: gen.generate_sentence(start_with_lorem=True),
        lambda gen: gen.generate_paragraphs(2),
        lambda gen: gen.generate_html_paragraphs(2),
        lambda gen: gen.generate_list(4, ordered=True),
    )
    for method in methods:
        assert method(LoremGenerator(seed=123)) == method(LoremGenerator(seed=123))
