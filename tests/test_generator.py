import pytest
from lorem_generator.generator import LoremGenerator


def test_generate_words():
    """Test word generation."""
    gen = LoremGenerator(seed=42)
    words = gen.generate_words(10)
    assert len(words.split()) == 10


def test_generate_sentence():
    """Test sentence generation."""
    gen = LoremGenerator(seed=42)
    sentence = gen.generate_sentence()
    assert sentence.endswith(".")
    assert sentence[0].isupper()


def test_generate_paragraph():
    """Test paragraph generation."""
    gen = LoremGenerator(seed=42)
    paragraph = gen.generate_paragraph()
    assert "." in paragraph


def test_generate_paragraphs():
    """Test multiple paragraphs."""
    gen = LoremGenerator(seed=42)
    paragraphs = gen.generate_paragraphs(3)
    assert "\n\n" in paragraphs


def test_seed_reproducibility():
    """Test that seed produces same output."""
    gen1 = LoremGenerator(seed=123)
    gen2 = LoremGenerator(seed=123)
    assert gen1.generate_words(5) == gen2.generate_words(5)
