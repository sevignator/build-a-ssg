import re
from classes.textnode import TextNode


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
