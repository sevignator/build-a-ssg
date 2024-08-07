from utils.custom_types import BlockType


def block_to_block_type(block: str) -> BlockType:
    if block.startswith("#"):
        return "heading"
    elif block.startswith("```") and block.endswith("```"):
        return "code"
    elif block.startswith(">"):
        return "quote"
    elif block.startswith("*") or block.startswith("-"):
        return "unordered_list"
    elif block.startswith("1. "):
        return "ordered_list"
    else:
        return "paragraph"
