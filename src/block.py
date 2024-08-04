import re
from typing import Literal
from custom_types import BlockType
from inline import text_to_textnodes
from leafnode import LeafNode
from parentnode import ParentNode


def markdown_to_blocks(markdown: str):
    """Converts a Markdown string into a list of block strings."""

    blocks = markdown.split("\n\n")
    output = list(filter(lambda x: x != "", map(lambda x: x.strip(), blocks)))
    return output


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


def markdown_to_html_node(markdown: str):
    container_node = ParentNode("div", [])
    blocks = markdown_to_blocks(markdown)

    for block in blocks:
        block_type = block_to_block_type(block)
        current_node = None

        match block_type:
            case "paragraph":
                current_node = ParentNode("p", text_to_children(block))
            case "heading":
                heading = extract_heading(block)

                current_node = ParentNode(
                    f"h{heading["level"]}", text_to_children(heading["text"])
                )
            case "code":
                current_node = ParentNode("pre", text_to_children(block))
            case "quote":
                current_node = ParentNode("blockquote", text_to_children(block))
            case "unordered_list":
                current_node = ParentNode(
                    "ul",
                    list(
                        map(
                            lambda x: ParentNode("li", text_to_children(x)),
                            extract_list_items(block, "ul"),
                        )
                    ),
                )
            case "ordered_list":
                current_node = ParentNode(
                    "ol",
                    list(
                        map(
                            lambda x: ParentNode("li", text_to_children(x)),
                            extract_list_items(block, "ol"),
                        )
                    ),
                )

        if current_node is None:
            raise ValueError(f"The {block_type} does not exist.")

        container_node.children.append(current_node)

    return container_node


def extract_list_items(block: str, list_type: Literal["ul", "ol"]) -> list[str]:
    match list_type:
        case "ul":
            return list(filter(lambda x: x != "", re.split(r"\s*[-\*]\s", block)))
        case "ol":
            return list(filter(lambda x: x != "", re.split(r"\s*[\d]+\.\s", block)))
        case _:
            raise ValueError(f"The {list_type} type is invalid.")


def extract_heading(block: str):
    parts = tuple(filter(lambda x: x != "", re.split(r"^(#+)\s", block)))
    level = len(parts[0])
    text = parts[1]

    if level > 6:
        raise ValueError(f"Invalid heading level `{level}`.")

    return {"level": level, "text": text}


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
