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
            new_nodes.append(node)
            continue

        # Handle case where there's an uneven amount of delimiters
        if delimiter_count % 2 == 1:
            raise ValueError(f"A closing {delimiter} delimiter is missing.")

        for chunk in split_node:
            if chunk.startswith(" ") or chunk.endswith(" "):
                new_nodes.append(TextNode(chunk, "text"))
                continue

            new_nodes.append(TextNode(chunk, text_type))

    return new_nodes


def split_nodes_image(old_nodes: list[TextNode]):
    new_nodes: list[TextNode] = []

    for node in old_nodes:
        split_node = list(
            filter(lambda x: x != "", re.split(r"(!\[.*?\]\(.*?\))", node.text))
        )

        # Handle case where the node isn't divisible (i.e. no images)
        if len(split_node) == 1:
            new_nodes.append(node)
            continue

        # Handle case where the node isn't of type "text"
        if node.text_type != "text":
            new_nodes.append(node)
            continue

        for chunk in split_node:
            if chunk.startswith(" ") or chunk.endswith(" "):
                new_nodes.append(TextNode(chunk, "text"))
                continue

            img_alt_text = re.findall(r"\[(.*?)\]", chunk)[0]
            img_url = re.findall(r"\((.*?)\)", chunk)[0]
            new_nodes.append(TextNode(img_alt_text, "image", img_url))

    return new_nodes


def split_nodes_link(old_nodes: list[TextNode]):
    new_nodes: list[TextNode] = []

    for node in old_nodes:
        split_node = list(
            filter(lambda x: x != "", re.split(r"(\[.*?\]\(.*?\))", node.text))
        )

        # Handle case where the node isn't divisible (i.e. no links)
        if len(split_node) == 1:
            new_nodes.append(node)
            continue

        # Handle case where the node isn't of type "text"
        if node.text_type != "text":
            new_nodes.append(node)
            continue

        for chunk in split_node:
            if chunk.startswith(" ") or chunk.endswith(" "):
                new_nodes.append(TextNode(chunk, "text"))
                continue

            link_text = re.findall(r"\[(.*?)\]", chunk)[0]
            link_url = re.findall(r"\((.*?)\)", chunk)[0]
            new_nodes.append(TextNode(link_text, "link", link_url))

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

    return re.findall(r"[!]\[(.*?)\]\((.*?)\)", text)


def extract_markdown_links(text: str) -> list[tuple[str, str]]:
    """Extracts Markdown links from a string and returns each text/href pairs as tuples."""

    return re.findall(r"[^!]\[(.*?)\]\((.*?)\)", text)


def text_to_textnodes(text: str):
    initial_node = TextNode(text, "text")
    nodes_with_bold = split_nodes_delimiter([initial_node], "**", "bold")
    nodes_with_italic = split_nodes_delimiter(nodes_with_bold, "*", "italic")
    nodes_with_code_block = split_nodes_delimiter(nodes_with_italic, "`", "code")
    nodes_with_image = split_nodes_image(nodes_with_code_block)
    nodes_with_link = split_nodes_link(nodes_with_image)

    return nodes_with_link
    # Example input:
    # This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)

    # Example output:
    # [
    #     TextNode("This is ", text_type_text),
    #     TextNode("text", text_type_bold),
    #     TextNode(" with an ", text_type_text),
    #     TextNode("italic", text_type_italic),
    #     TextNode(" word and a ", text_type_text),
    #     TextNode("code block", text_type_code),
    #     TextNode(" and an ", text_type_text),
    #     TextNode("obi wan image", text_type_image, "https://i.imgur.com/fJRm4Vk.jpeg"),
    #     TextNode(" and a ", text_type_text),
    #     TextNode("link", text_type_link, "https://boot.dev"),
    # ]


# [
#     TextNode("This is ", "text"),
#     TextNode("text", "bold"),
#     TextNode(" with an ", "text"),
#     TextNode("italic", "italic"),
#     TextNode(" word and a ", "text"),
#     TextNode("code block", "code"),
#     TextNode(" and an ", "text"),
#     TextNode("obi wan image", "image", "https://i.imgur.com/fJRm4Vk.jpeg"),
#     TextNode(" and a ", "text"),
#     TextNode("link", "link", "https://boot.dev"),
# ]
