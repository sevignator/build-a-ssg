import re


# TODO: Find out where to use this function
def extract_markdown_links(text: str) -> list[tuple[str, str]]:
    """Extracts Markdown links from a string and returns each text/href pairs as tuples."""

    return re.findall(r"[^!]\[(.*?)\]\((.*?)\)", text)
