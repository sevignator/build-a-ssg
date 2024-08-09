from classes.parentnode import ParentNode
from functions.block_to_block_type import block_to_block_type
from functions.extract_heading import extract_heading
from functions.extract_list_items import extract_list_items
from functions.markdown_to_blocks import markdown_to_blocks
from functions.text_to_children import text_to_children
from utils.remove_empty_strings import remove_empty_strings


def markdown_to_html_node(markdown: str):
    """Takes a Markdown input, converts it into blocks, determines which tag should
    be applied to each block and returns a `ParentNode` containing those blocks."""

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
                paragraphs = remove_empty_strings(block.split("> "))
                children: list = []

                for p in paragraphs:
                    children.append(*text_to_children(p))

                current_node = ParentNode("blockquote", children)
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

        if container_node.children is not None:
            container_node.children.append(current_node)

    return container_node
