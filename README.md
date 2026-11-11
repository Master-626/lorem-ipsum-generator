# Lorem Ipsum Generator

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)

## 中文简介

这是一个给设计师和开发者用的 Lorem Ipsum 占位文本工具，可以作为命令行程序，也可以作为 Python 库。它能生成单词、句子、段落、HTML 段落和列表，以及**恰好指定字符数**的文本。同一随机种子会得到相同结果。需要 Python 3.8 或更高版本。

```bash
pip install .
lorem words -n 10
lorem chars -n 80
pip install -e ".[dev]" && pytest && ruff check .
```

## Overview

`lorem-ipsum-generator` builds placeholder text from the classic Lorem Ipsum vocabulary. Use it to fill a layout, a fixture, or a test without writing copy.

Sentences are capitalized word sequences ending in a period. They are not grammatical Latin. The same `seed` passed to `LoremGenerator` reproduces a result.

## Installation

Python 3.8 or newer is required.

```bash
git clone https://github.com/Master-626/lorem-ipsum-generator.git
cd lorem-ipsum-generator
pip install .
```

The install provides two equivalent commands: `lorem` and `lorem-ipsum`.

For development, including tests and Ruff:

```bash
pip install -e ".[dev]"
```

## Usage

Count options accept `0` and reject negative numbers. Defaults are shown below.

### Words

```bash
lorem words -n 10
```

### Exact character length

`chars` prints exactly `-n` characters. Words are separated by single spaces and the text may stop mid-word, which is what you want when a mock must fit a fixed field.

```bash
lorem chars -n 80
```

### Sentences

```bash
lorem sentences -n 3
```

### Paragraphs

```bash
lorem paragraphs -n 2
```

Paragraphs are separated by a blank line.

### HTML

```bash
lorem html -n 3
lorem list -n 5
lorem list -n 5 --ordered
```

Each list item contains five words. `--ordered` switches the tag from `<ul>` to `<ol>`.

### Version

```bash
lorem --version
```

## Options

| Command | Option | Default | Meaning |
| --- | --- | --- | --- |
| `words` | `-n`, `--count` | `10` | Number of words |
| `chars` | `-n`, `--count` | `100` | Exact number of characters |
| `sentences` | `-n`, `--count` | `1` | Number of sentences |
| `paragraphs` | `-n`, `--count` | `3` | Number of paragraphs |
| `html` | `-n`, `--count` | `3` | Number of `<p>` elements |
| `list` | `-n`, `--count` | `5` | Number of `<li>` elements |
| `list` | `--ordered` | off | Use `<ol>` instead of `<ul>` |
| *(all)* | `--help` | | Show command help |
| *(root)* | `--version` | | Print the package version and exit |

## Python API

```python
from lorem_generator import LoremGenerator

gen = LoremGenerator(seed=42)

gen.generate_words(10)
gen.generate_chars(80)
gen.generate_sentence()
gen.generate_sentence(min_words=3, max_words=3, start_with_lorem=True)
gen.generate_paragraph()
gen.generate_paragraphs(3)
gen.generate_html_paragraphs(2)
gen.generate_list(5, ordered=True)
```

| Method | Arguments | Result |
| --- | --- | --- |
| `LoremGenerator` | `seed=None` | `seed=None` uses nondeterministic randomness. Any value accepted by `random.Random` is stable across calls. |
| `generate_words` | `count=10` | `count` vocabulary words joined by spaces. `count=0` returns `""`. |
| `generate_chars` | `count=100` | A string of length `count`. `count=0` returns `""`. |
| `generate_sentence` | `min_words=8`, `max_words=15`, `start_with_lorem=False` | One sentence whose word count is between the two bounds. Both bounds must be at least 1 and `min_words` cannot exceed `max_words`. `start_with_lorem=True` begins with "Lorem ipsum dolor sit amet", shortened to the requested length when that length is under five words. |
| `generate_paragraph` | `min_sentences=3`, `max_sentences=6` | One paragraph. Bounds follow the same rules as sentence word bounds. |
| `generate_paragraphs` | `count=3` | Paragraphs separated by a blank line. |
| `generate_html_paragraphs` | `count=3` | The same paragraphs, each wrapped in `<p>`. |
| `generate_list` | `count=5`, `ordered=False` | An HTML list. `count=0` returns `<ul></ul>` or `<ol></ol>`. |

Negative counts, and bounds below 1, raise `ValueError`. Non-integers raise `TypeError`.

## Running tests

```bash
pip install -e ".[dev]"
pytest
ruff check .
```

`pytest` reads `tests/` and adds `src/` to `sys.path`. The dev extra installs pytest and Ruff. Continuous integration runs both on Python 3.8 through 3.13.

## License

MIT License. Copyright (c) 2026 Xu Jiaqi.
