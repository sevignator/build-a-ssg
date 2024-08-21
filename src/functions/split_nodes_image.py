import re

from classes.textnode import TextNode
from functions.extract_markdown_images import extract_markdown_images
from utils.should_be_text import should_be_text
from utils.remove_empty_strings import remove_empty_strings


def split_nodes_image(old_nodes: list[TextNode]):
    new_nodes: list[TextNode] = []

    for node in old_nodes:
        split_node = remove_empty_strings(re.split(r"(!\[.*?\]\(.*?\))", node.text))

        # Handle case where the node cannot be divided and isn't an image
        if len(split_node) == 1 and not re.match(r"!\[.*?\]\(.*?\)", split_node[0]):
            new_nodes.append(node)
            continue

        # Handle case where the node isn't of type "text"
        if node.text_type != "text":
            new_nodes.append(node)
            continue

        for chunk in split_node:
            if should_be_text(chunk):
                new_nodes.append(TextNode(chunk, "text"))
                continue

            # Handle images
            (alt_text, url) = extract_markdown_images(chunk)[0]
            new_nodes.append(TextNode(alt_text, "image", url))

    return new_nodes
