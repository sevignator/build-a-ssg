import re

from classes.textnode import TextNode
from functions.extract_markdown_links import extract_markdown_links
from utils.remove_empty_strings import remove_empty_strings


def split_nodes_link(old_nodes: list[TextNode]):
    new_nodes: list[TextNode] = []

    for node in old_nodes:
        split_node = remove_empty_strings(re.split(r"(\[.*?\]\(.*?\))", node.text))

        # Handle case where the node cannot be divided and isn't a link
        if len(split_node) == 1 and not re.match(r"(\[.*?\]\(.*?\))", split_node[0]):
            new_nodes.append(node)
            continue

        # Handle case where the node isn't of type "text"
        if node.text_type != "text":
            new_nodes.append(node)
            continue

        for chunk in split_node:
            if chunk.startswith((" ", ".")) or chunk.endswith(" "):
                new_nodes.append(TextNode(chunk, "text"))
                continue

            # Handle links
            (text, url) = extract_markdown_links(chunk)[0]
            new_nodes.append(TextNode(text, "link", url))

    return new_nodes
