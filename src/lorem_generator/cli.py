"""
CLI interface for lorem-ipsum-generator.
"""

import click

from . import __version__
from .generator import LoremGenerator


# Click would otherwise look up a distribution named "lorem_generator".
# The installed project name is "lorem-ipsum-generator", so pass the
# version from this package instead of guessing.
@click.group()
@click.version_option(__version__)
def main():
    """Lorem Ipsum Generator - Placeholder text for designers and developers."""
    pass


@main.command()
@click.option(
    "-n",
    "--count",
    default=10,
    show_default=True,
    type=click.IntRange(min=0),
    help="Number of words",
)
def words(count):
    """Generate random words."""
    gen = LoremGenerator()
    click.echo(gen.generate_words(count))


@main.command()
@click.option(
    "-n",
    "--count",
    default=100,
    show_default=True,
    type=click.IntRange(min=0),
    help="Number of characters",
)
def chars(count):
    """Generate placeholder text of an exact character length."""
    gen = LoremGenerator()
    click.echo(gen.generate_chars(count))


@main.command()
@click.option(
    "-n",
    "--count",
    default=1,
    show_default=True,
    type=click.IntRange(min=0),
    help="Number of sentences",
)
def sentences(count):
    """Generate random sentences."""
    gen = LoremGenerator()
    result = " ".join([gen.generate_sentence() for _ in range(count)])
    click.echo(result)


@main.command()
@click.option(
    "-n",
    "--count",
    default=3,
    show_default=True,
    type=click.IntRange(min=0),
    help="Number of paragraphs",
)
def paragraphs(count):
    """Generate random paragraphs."""
    gen = LoremGenerator()
    click.echo(gen.generate_paragraphs(count))


@main.command()
@click.option(
    "-n",
    "--count",
    default=3,
    show_default=True,
    type=click.IntRange(min=0),
    help="Number of paragraphs",
)
def html(count):
    """Generate HTML paragraphs."""
    gen = LoremGenerator()
    click.echo(gen.generate_html_paragraphs(count))


@main.command("list")
@click.option(
    "-n",
    "--count",
    default=5,
    show_default=True,
    type=click.IntRange(min=0),
    help="Number of list items",
)
@click.option("--ordered", is_flag=True, help="Generate an ordered list")
def list_items(count, ordered):
    """Generate an HTML list."""
    gen = LoremGenerator()
    click.echo(gen.generate_list(count, ordered=ordered))


if __name__ == "__main__":
    main()
