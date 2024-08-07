import re

from typing import Literal


def extract_list_items(block: str, list_type: Literal["ul", "ol"]) -> list[str]:
    match list_type:
        case "ul":
            return list(filter(lambda x: x != "", re.split(r"\s*[-\*]\s", block)))
        case "ol":
            return list(filter(lambda x: x != "", re.split(r"\s*[\d]+\.\s", block)))
        case _:
            raise ValueError(f"The {list_type} type is invalid.")
