from src.textnode import TextNode
from src.leafnode import LeafNode


def text_node_to_html_node(text_node: TextNode) -> LeafNode:
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
        case _:
            raise ValueError(f'The provided "{text_node.text_type}" type is invalid.')
