import re

from textnode import TextNode
from leafnode import LeafNode
from custom_types import Delimiters, TextType


def text_node_to_html_node(text_node: TextNode):
    """Transforms a TextNode object into its analogous LeafNode representation."""

    match text_node.text_type:
        case "text":
            return LeafNode(None, text_node.text)
        case "bold":
            return LeafNode("b", text_node.text)
        case "italic":
            return LeafNode("i", text_node.text)
        case "code":
            return LeafNode("code", text_node.text)
        case "link":
            if text_node.url is None:
                raise ValueError("Link nodes are required to have a URL.")
            return LeafNode("a", text_node.text, {"href": text_node.url})
        case "image":
            if text_node.url is None:
                raise ValueError("Link nodes are required to have a URL.")
            return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})


def split_nodes_delimiter(
    old_nodes: list[TextNode], delimiter: Delimiters, text_type: TextType
):
    """Splits a TextNode's text into multiple typed ones based on a delimiter."""

    new_nodes: list[TextNode] = []

    for node in old_nodes:
        pattern = re.compile(delimiter_to_regex_pattern(delimiter))
        delimiter_count = len(pattern.findall(node.text))
        split_node = list(filter(lambda x: x != "", node.text.split(delimiter)))

        # Handle case where the node isn't of type "text"
        if node.text_type != "text":
            new_nodes.append(node)
            continue

        # Handle case where the delimiter is not found in the string
        if delimiter_count == 0:
            raise ValueError(f"The {delimiter} delimiter could not be found.")

        # Handle case where there's an uneven amount of delimiters
        if delimiter_count % 2 == 1:
            raise ValueError(f"A closing {delimiter} delimiter is missing.")

        for chunk in split_node:
            if chunk.startswith(" ") or chunk.endswith(" "):
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
            return delimiter


def extract_markdown_images(text: str) -> list[tuple[str, str]]:
    """Extracts Markdown images from a string and returns each text/href pairs as tuples."""

    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)


def extract_markdown_links(text: str) -> list[tuple[str, str]]:
    """Extracts Markdown links from a string and returns each text/href pairs as tuples."""

    return re.findall(r"\[(.*?)\]\((.*?)\)", text)
