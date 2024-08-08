import re


# TODO: Find out where to use this function
def extract_markdown_images(text: str) -> list[tuple[str, str]]:
    """Extracts Markdown images from a string and returns each text/href pairs as tuples."""

    return re.findall(r"[!]\[(.*?)\]\((.*?)\)", text)
