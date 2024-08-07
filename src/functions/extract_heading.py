import re


def extract_heading(block: str):
    parts = tuple(filter(lambda x: x != "", re.split(r"^(#+)\s", block)))
    level = len(parts[0])
    text = parts[1]

    if level > 6:
        raise ValueError(f"Invalid heading level `{level}`.")

    return {"level": level, "text": text}
