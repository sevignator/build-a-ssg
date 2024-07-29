from utils import split_nodes_delimiter
from textnode import TextNode


def main() -> None:
    node = TextNode("**This entire sentence is bold**", "text")
    new_nodes = split_nodes_delimiter([node], "**", "bold")
    print("Testing from main.py")
    print("Original:", node)
    print("New:", new_nodes)


main()
