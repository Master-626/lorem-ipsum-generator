"""
Core Lorem Ipsum generation logic.
"""

import random
from typing import Optional

# Classic Lorem Ipsum words
LOREM_WORDS = [
    "lorem", "ipsum", "dolor", "sit", "amet", "consectetur", "adipiscing",
    "elit", "sed", "do", "eiusmod", "tempor", "incididunt", "ut", "labore",
    "et", "dolore", "magna", "aliqua", "enim", "ad", "minim", "veniam",
    "quis", "nostrud", "exercitation", "ullamco", "laboris", "nisi",
    "aliquip", "ex", "ea", "commodo", "consequat", "duis", "aute", "irure",
    "in", "reprehenderit", "voluptate", "esse", "cillum", "fugiat", "pariatur",
    "excepteur", "sint", "occaecat", "cupidatat", "non", "proident", "sunt",
    "culpa", "qui", "officia", "deserunt", "mollit", "anim", "id", "est",
    "laborum",
]

# Opening of the traditional passage. Kept lowercase so sentence
# capitalization is applied once, in one place.
_CLASSIC_PREFIX = ("lorem", "ipsum", "dolor", "sit", "amet")


def _require_int(name, value):
    # bool is a subclass of int and was previously accepted by range().
    if not isinstance(value, int):
        raise TypeError(f"{name} must be an int")


def _require_non_negative(name, value):
    _require_int(name, value)
    if value < 0:
        raise ValueError(f"{name} must be non-negative")


def _require_positive_range(min_name, min_value, max_name, max_value):
    _require_int(min_name, min_value)
    _require_int(max_name, max_value)
    if min_value < 1:
        raise ValueError(f"{min_name} must be at least 1")
    if max_value < 1:
        raise ValueError(f"{max_name} must be at least 1")
    if min_value > max_value:
        raise ValueError(
            f"{min_name} ({min_value}) cannot be greater than {max_name} ({max_value})"
        )


class LoremGenerator:
    """Generate Lorem Ipsum placeholder text."""

    def __init__(self, seed: Optional[int] = None):
        self.random = random.Random(seed)

    def generate_words(self, count: int = 10) -> str:
        """Generate ``count`` random words separated by spaces."""
        _require_non_negative("count", count)
        words = [self.random.choice(LOREM_WORDS) for _ in range(count)]
        return " ".join(words)

    def generate_chars(self, count: int = 100) -> str:
        """Generate placeholder text of exactly ``count`` characters.

        Words are drawn from the same vocabulary as generate_words and
        separated by single spaces. The result is a prefix of that
        stream, so it may end in the middle of a word or on a space.
        """
        _require_non_negative("count", count)
        if count == 0:
            return ""

        chunks = []
        length = 0
        while length < count:
            word = self.random.choice(LOREM_WORDS)
            if chunks:
                chunks.append(" ")
                length += 1
            chunks.append(word)
            length += len(word)
        return "".join(chunks)[:count]

    def generate_sentence(
        self,
        min_words: int = 8,
        max_words: int = 15,
        start_with_lorem: bool = False,
    ) -> str:
        """Generate a random sentence.

        With ``start_with_lorem``, the sentence begins with the classic
        "Lorem ipsum..." phrase, truncated when fewer than five words
        were requested. The total number of words stays inside
        ``min_words``..``max_words``.
        """
        _require_positive_range("min_words", min_words, "max_words", max_words)
        word_count = self.random.randint(min_words, max_words)
        words = self.generate_words(word_count).split()

        if start_with_lorem:
            words = list(_CLASSIC_PREFIX[:word_count]) + words[len(_CLASSIC_PREFIX):]

        return " ".join(words).capitalize() + "."

    def generate_paragraph(
        self,
        min_sentences: int = 3,
        max_sentences: int = 6,
    ) -> str:
        """Generate a random paragraph."""
        _require_positive_range(
            "min_sentences", min_sentences, "max_sentences", max_sentences
        )
        sentence_count = self.random.randint(min_sentences, max_sentences)
        sentences = [self.generate_sentence() for _ in range(sentence_count)]
        return " ".join(sentences)

    def generate_paragraphs(self, count: int = 3) -> str:
        """Generate multiple paragraphs separated by a blank line."""
        _require_non_negative("count", count)
        paragraphs = [self.generate_paragraph() for _ in range(count)]
        return "\n\n".join(paragraphs)

    def generate_html_paragraphs(self, count: int = 3) -> str:
        """Generate HTML paragraphs."""
        _require_non_negative("count", count)
        paragraphs = [self.generate_paragraph() for _ in range(count)]
        return "\n".join(f"<p>{p}</p>" for p in paragraphs)

    def generate_list(self, count: int = 5, ordered: bool = False) -> str:
        """Generate an HTML list with five words in each item."""
        _require_non_negative("count", count)
        items = [self.generate_words(5) for _ in range(count)]
        tag = "ol" if ordered else "ul"
        if not items:
            return f"<{tag}></{tag}>"
        items_html = "\n".join(f"  <li>{item}</li>" for item in items)
        return f"<{tag}>\n{items_html}\n</{tag}>"
