import re

from typing import Literal

from utils.remove_empty_strings import remove_empty_strings


def extract_list_items(block: str, list_type: Literal["ul", "ol"]) -> list[str]:
    match list_type:
        case "ul":
            return remove_empty_strings(re.split(r"\s*[-\*]\s", block))
        case "ol":
            return remove_empty_strings(re.split(r"\s*[\d]+\.\s", block))
        case _:
            raise ValueError(f"The {list_type} type is invalid.")
