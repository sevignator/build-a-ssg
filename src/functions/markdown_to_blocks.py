from utils.remove_empty_strings import remove_empty_strings


def markdown_to_blocks(markdown: str):
    """Converts a Markdown string into a list of block strings."""

    blocks = markdown.split("\n\n")
    return remove_empty_strings(map(lambda x: x.strip(), blocks))
