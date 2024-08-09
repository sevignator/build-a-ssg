from functions.text_to_textnodes import text_to_textnodes
from functions.text_node_to_html_node import text_node_to_html_node


def text_to_children(text):
    """Takes a string of text and returns a list of `HTMLNode`s with inline elements."""

    text_nodes = text_to_textnodes(text)
    html_nodes = []

    for node in text_nodes:
        html_nodes.append(text_node_to_html_node(node))

    return html_nodes
