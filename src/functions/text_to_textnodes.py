from classes.textnode import TextNode
from functions.split_nodes_delimiter import split_nodes_delimiter
from functions.split_nodes_image import split_nodes_image
from functions.split_nodes_link import split_nodes_link


def text_to_textnodes(text: str):
    """Creates a `TextNode` using the provided string, extracts every inline nodes within it and returns them as a list of `TextNodes`."""

    initial_node = TextNode(text, "text")
    nodes_with_bold = split_nodes_delimiter([initial_node], "**", "bold")
    nodes_with_italic = split_nodes_delimiter(nodes_with_bold, "*", "italic")
    nodes_with_code_block = split_nodes_delimiter(nodes_with_italic, "`", "code")
    nodes_with_image = split_nodes_image(nodes_with_code_block)
    nodes_with_link = split_nodes_link(nodes_with_image)

    return nodes_with_link
