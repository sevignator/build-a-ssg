import unittest

from textnode import TextNode
from utils import split_nodes_delimiter


class TestSplitNodes(unittest.TestCase):
    def test_single_node_bold(self):
        node = TextNode("This is text with a **bold** word", "text")
        new_nodes = split_nodes_delimiter([node], "**", "bold")
        self.assertEqual(
            repr(new_nodes),
            "[TextNode(This is text with a , text, None), TextNode(bold, bold, None), TextNode( word, text, None)]",
        )

    def test_single_node_italic(self):
        node = TextNode("This is text with a *italic* word", "text")
        new_nodes = split_nodes_delimiter([node], "*", "italic")
        self.assertEqual(
            repr(new_nodes),
            "[TextNode(This is text with a , text, None), TextNode(italic, italic, None), TextNode( word, text, None)]",
        )

    def test_single_node_code(self):
        node = TextNode("This is text with a `code block` word", "text")
        new_nodes = split_nodes_delimiter([node], "`", "code")
        self.assertEqual(
            repr(new_nodes),
            "[TextNode(This is text with a , text, None), TextNode(code block, code, None), TextNode( word, text, None)]",
        )

    def test_single_node_full_width(self):
        node = TextNode("**This entire sentence is bold**", "text")
        new_nodes = split_nodes_delimiter([node], "**", "bold")
        self.assertEqual(
            repr(new_nodes), "[TextNode(This entire sentence is bold, bold, None)]"
        )

    def test_single_node_non_text(self):
        node = TextNode("This is `code block` within a code text node", "code")
        new_nodes = split_nodes_delimiter([node], "`", "code")
        self.assertEqual(
            repr(new_nodes),
            "[TextNode(This is `code block` within a code text node, code, None)]",
        )

    def test_multiple_nodes(self):
        node_1 = TextNode("This is text with a `bold` word", "text")
        node_2 = TextNode("More text with a `bold` word", "text")
        new_nodes = split_nodes_delimiter([node_1, node_2], "`", "bold")
        self.assertEqual(
            repr(new_nodes),
            "[TextNode(This is text with a , text, None), TextNode(bold, bold, None), TextNode( word, text, None), TextNode(More text with a , text, None), TextNode(bold, bold, None), TextNode( word, text, None)]",
        )

    def test_delimiter_not_found(self):
        node = TextNode("This is text with an *invalid delimiter", "text")
        self.assertRaises(
            ValueError, lambda: split_nodes_delimiter([node], "*", "bold")
        )

    def test_uneven_delimiters(self):
        node = TextNode("This is text with no delimiter", "text")
        self.assertRaises(
            ValueError, lambda: split_nodes_delimiter([node], "*", "bold")
        )


if __name__ == "__main__":
    unittest.main()
