import re
from functions.extract_heading import extract_heading
from functions.markdown_to_blocks import markdown_to_blocks


def extract_title(markdown: str):
    """Extracts a Markdown file's title (h1) and returns its content."""

    blocks = markdown_to_blocks(markdown)
    title_block = list(filter(lambda x: re.match(r"^# ", x), blocks))[0]
    title_heading = extract_heading(title_block)
    return title_heading["text"]
