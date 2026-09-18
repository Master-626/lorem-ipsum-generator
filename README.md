# Lorem Ipsum Generator

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![Made for Designers](https://img.shields.io/badge/made%20for-designers-purple.svg)]()

A Lorem Ipsum placeholder text generator for designers and developers worldwide.

## 🌟 Features

- 📝 **Words** - Generate random words
- ✏️ **Sentences** - Generate grammatical sentences
- 📄 **Paragraphs** - Generate multiple paragraphs
- 🌐 **HTML Output** - Generate ready-to-use HTML
- 🎲 **Reproducible** - Seed support for consistent output
- 🐍 **Python API** - Use as a library in your code

## 📦 Installation

```bash
git clone https://github.com/Master-626/lorem-ipsum-generator.git
cd lorem-ipsum-generator
pip install .
```

## 🚀 Usage

### Generate Words
```bash
# 10 random words
lorem words -n 10
```

### Generate Sentences
```bash
# 3 sentences
lorem sentences -n 3
```

### Generate Paragraphs
```bash
# 5 paragraphs
lorem paragraphs -n 5
```

### Generate HTML
```bash
# HTML paragraphs
lorem html -n 3

# HTML list
lorem list -n 5 --ordered
```

## 🐍 Python API

```python
from lorem_generator import LoremGenerator

# Create generator with seed
gen = LoremGenerator(seed=42)

# Generate different types
print(gen.generate_words(10))
print(gen.generate_sentence())
print(gen.generate_paragraphs(3))
print(gen.generate_html_paragraphs(2))
```

## 🧪 Testing

```bash
pip install -e ".[dev]"
pytest
```

## 📄 License

MIT License
