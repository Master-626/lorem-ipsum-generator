"""
Core Lorem Ipsum generation logic.
"""

import random
from typing import List, Optional


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


class LoremGenerator:
    """Generate Lorem Ipsum placeholder text."""

    def __init__(self, seed: Optional[int] = None):
        self.random = random.Random(seed)

    def generate_words(self, count: int = 10) -> str:
        """Generate random words."""
        words = [self.random.choice(LOREM_WORDS) for _ in range(count)]
        return " ".join(words)

    def generate_sentence(
        self,
        min_words: int = 8,
        max_words: int = 15,
        start_with_lorem: bool = False,
    ) -> str:
        """Generate a random sentence."""
        word_count = self.random.randint(min_words, max_words)
        words = self.generate_words(word_count).split()

        if start_with_lorem:
            words = ["Lorem", "ipsum", "dolor", "sit", "amet"] + words[5:]

        sentence = " ".join(words).capitalize() + "."
        return sentence

    def generate_paragraph(
        self,
        min_sentences: int = 3,
        max_sentences: int = 6,
    ) -> str:
        """Generate a random paragraph."""
        sentence_count = self.random.randint(min_sentences, max_sentences)
        sentences = [self.generate_sentence() for _ in range(sentence_count)]
        return " ".join(sentences)

    def generate_paragraphs(self, count: int = 3) -> str:
        """Generate multiple paragraphs."""
        paragraphs = [self.generate_paragraph() for _ in range(count)]
        return "\n\n".join(paragraphs)

    def generate_html_paragraphs(self, count: int = 3) -> str:
        """Generate HTML paragraphs."""
        paragraphs = [self.generate_paragraph() for _ in range(count)]
        return "\n".join(f"<p>{p}</p>" for p in paragraphs)

    def generate_list(self, count: int = 5, ordered: bool = False) -> str:
        """Generate an HTML list."""
        items = [self.generate_words(5) for _ in range(count)]
        tag = "ol" if ordered else "ul"
        items_html = "\n".join(f"  <li>{item}</li>" for item in items)
        return f"<{tag}>\n{items_html}\n</{tag}>"
