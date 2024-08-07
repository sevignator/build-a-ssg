from classes.parentnode import ParentNode
from functions.block_to_block_type import block_to_block_type
from functions.extract_heading import extract_heading
from functions.extract_list_items import extract_list_items
from functions.markdown_to_blocks import markdown_to_blocks
from functions.text_to_children import text_to_children


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

        if container_node.children is not None:
            container_node.children.append(current_node)

    return container_node
