from classes.leafnode import LeafNode
from functions.text_to_textnodes import text_to_textnodes


def text_to_children(text):
    """Takes a string of text and returns a list of `HTMLNode`s with inline elements."""

    text_nodes = text_to_textnodes(text)
    html_nodes = []

    for node in text_nodes:
        match node.text_type:
            case "text":
                html_nodes.append(LeafNode(None, node.text))
            case "bold":
                html_nodes.append(LeafNode("b", node.text))
            case "italic":
                html_nodes.append(LeafNode("i", node.text))
            case "code":
                html_nodes.append(LeafNode("code", node.text))
            case "image":
                html_nodes.append(LeafNode("img", node.text, {"href": node.url}))
            case "link":
                html_nodes.append(LeafNode("a", node.text, {"href": node.url}))

    return html_nodes
