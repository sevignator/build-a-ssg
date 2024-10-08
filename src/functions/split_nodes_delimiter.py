import re
from classes.textnode import TextNode
from utils.should_be_text import should_be_text
from utils.custom_types import Delimiters, TextType


def split_nodes_delimiter(
    old_nodes: list[TextNode], delimiter: Delimiters, text_type: TextType
):
    """Splits a `TextNode`'s text into multiple typed ones based on a delimiter."""

    new_nodes: list[TextNode] = []

    for node in old_nodes:
        pattern = delimiter_to_regex_pattern(delimiter)
        delimiter_count = len(re.findall(pattern, node.text))
        split_node = list(filter(lambda x: x != "", re.split(pattern, node.text)))

        # Handle case where the node isn't of type "text"
        if node.text_type != "text":
            new_nodes.append(node)
            continue

        # Handle case where the delimiter is not found in the string
        if delimiter_count == 0:
            new_nodes.append(node)
            continue

        for chunk in split_node:
            if should_be_text(chunk):
                new_nodes.append(TextNode(chunk, "text"))
                continue

            new_nodes.append(TextNode(chunk, text_type))

    return new_nodes


def delimiter_to_regex_pattern(delimiter: Delimiters):
    """Converts the provided delimiter into its regex-compatible equivalent."""

    match delimiter:
        case "*":
            return r"\*"
        case "**":
            return r"\*\*"
        case _:
            return rf"{delimiter}"
