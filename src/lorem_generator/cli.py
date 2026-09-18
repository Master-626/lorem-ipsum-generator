"""
CLI interface for lorem-ipsum-generator.
"""

import click
from .generator import LoremGenerator


@click.group()
@click.version_option()
def main():
    """Lorem Ipsum Generator - Placeholder text for designers and developers."""
    pass


@main.command()
@click.option("-n", "--count", default=10, help="Number of words")
def words(count):
    """Generate random words."""
    gen = LoremGenerator()
    click.echo(gen.generate_words(count))


@main.command()
@click.option("-n", "--count", default=1, help="Number of sentences")
def sentences(count):
    """Generate random sentences."""
    gen = LoremGenerator()
    result = " ".join([gen.generate_sentence() for _ in range(count)])
    click.echo(result)


@main.command()
@click.option("-n", "--count", default=3, help="Number of paragraphs")
def paragraphs(count):
    """Generate random paragraphs."""
    gen = LoremGenerator()
    click.echo(gen.generate_paragraphs(count))


@main.command()
@click.option("-n", "--count", default=3, help="Number of paragraphs")
def html(count):
    """Generate HTML paragraphs."""
    gen = LoremGenerator()
    click.echo(gen.generate_html_paragraphs(count))


@main.command()
@click.option("-n", "--count", default=5, help="Number of list items")
@click.option("--ordered", is_flag=True, help="Generate ordered list")
def list(count, ordered):
    """Generate HTML list."""
    gen = LoremGenerator()
    click.echo(gen.generate_list(count, ordered=ordered))


if __name__ == "__main__":
    main()
