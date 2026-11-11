from click.testing import CliRunner

from lorem_generator import __version__
from lorem_generator.cli import main
from lorem_generator.generator import LOREM_WORDS


def _payload(result):
    assert result.output.endswith("\n")
    return result.output[:-1]


def test_version_option():
    result = CliRunner().invoke(main, ["--version"])
    assert result.exit_code == 0
    assert __version__ in result.output
    assert result.exception is None


def test_help_lists_commands_and_defaults():
    result = CliRunner().invoke(main, ["--help"])
    assert result.exit_code == 0
    for name in ("words", "chars", "sentences", "paragraphs", "html", "list"):
        assert name in result.output


def test_words_command():
    result = CliRunner().invoke(main, ["words", "-n", "4"])
    assert result.exit_code == 0
    words = _payload(result).split()
    assert len(words) == 4
    assert all(word in LOREM_WORDS for word in words)


def test_chars_command_exact_length():
    result = CliRunner().invoke(main, ["chars", "-n", "20"])
    assert result.exit_code == 0
    assert len(_payload(result)) == 20

    empty = CliRunner().invoke(main, ["chars", "-n", "0"])
    assert empty.exit_code == 0
    assert _payload(empty) == ""


def test_sentences_and_paragraphs_commands():
    sentences = CliRunner().invoke(main, ["sentences", "-n", "2"])
    assert sentences.exit_code == 0
    assert _payload(sentences).count(".") == 2

    paragraphs = CliRunner().invoke(main, ["paragraphs", "-n", "2"])
    assert paragraphs.exit_code == 0
    assert "\n\n" in _payload(paragraphs)


def test_html_and_list_commands():
    html = CliRunner().invoke(main, ["html", "-n", "2"])
    assert html.exit_code == 0
    assert _payload(html).count("<p>") == 2

    unordered = CliRunner().invoke(main, ["list", "-n", "2"])
    assert unordered.exit_code == 0
    body = _payload(unordered)
    assert body.startswith("<ul>")
    assert body.count("<li>") == 2

    ordered = CliRunner().invoke(main, ["list", "-n", "2", "--ordered"])
    assert ordered.exit_code == 0
    assert _payload(ordered).startswith("<ol>")


def test_negative_counts_are_rejected():
    for args in (
        ["words", "-n", "-1"],
        ["chars", "--count", "-3"],
        ["sentences", "-n", "-1"],
        ["paragraphs", "-n", "-2"],
        ["html", "-n", "-1"],
        ["list", "-n", "-4"],
    ):
        result = CliRunner().invoke(main, args)
        assert result.exit_code != 0
        assert "not in the range" in result.output
