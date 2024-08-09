import re

from utils.remove_empty_strings import remove_empty_strings


def extract_heading(block: str):
    parts = tuple(remove_empty_strings(re.split(r"^(#+)\s", block)))
    level = len(parts[0])
    text = parts[1]

    if level > 6:
        raise ValueError(f"Invalid heading level `{level}`.")

    return {"level": level, "text": text}
