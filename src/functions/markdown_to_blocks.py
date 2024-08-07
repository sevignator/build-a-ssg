def markdown_to_blocks(markdown: str):
    """Converts a Markdown string into a list of block strings."""

    blocks = markdown.split("\n\n")
    return list(filter(lambda x: x != "", map(lambda x: x.strip(), blocks)))
