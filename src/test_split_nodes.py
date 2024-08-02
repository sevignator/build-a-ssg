import unittest

from textnode import TextNode
from utils import split_nodes_delimiter, split_nodes_image, split_nodes_link


class TestSplitNodes(unittest.TestCase):
    def test_single_node_bold(self):
        node = TextNode("This is text with a **bold** word", "text")
        new_nodes = split_nodes_delimiter([node], "**", "bold")
        self.assertEqual(
            repr(new_nodes),
            '[TextNode("This is text with a ", "text"), TextNode("bold", "bold"), TextNode(" word", "text")]',
        )

    def test_single_node_italic(self):
        node = TextNode("This is text with a *italic* word", "text")
        new_nodes = split_nodes_delimiter([node], "*", "italic")
        self.assertEqual(
            repr(new_nodes),
            '[TextNode("This is text with a ", "text"), TextNode("italic", "italic"), TextNode(" word", "text")]',
        )

    def test_single_node_code(self):
        node = TextNode("This is text with a `code block` word", "text")
        new_nodes = split_nodes_delimiter([node], "`", "code")
        self.assertEqual(
            repr(new_nodes),
            '[TextNode("This is text with a ", "text"), TextNode("code block", "code"), TextNode(" word", "text")]',
        )

    def test_single_node_full_width(self):
        node = TextNode("**This entire sentence is bold**", "text")
        new_nodes = split_nodes_delimiter([node], "**", "bold")
        self.assertEqual(
            repr(new_nodes), '[TextNode("This entire sentence is bold", "bold")]'
        )

    def test_single_node_non_text(self):
        node = TextNode("This is `code block` within a code text node", "code")
        new_nodes = split_nodes_delimiter([node], "`", "code")
        self.assertEqual(
            repr(new_nodes),
            '[TextNode("This is `code block` within a code text node", "code")]',
        )

    def test_multiple_nodes(self):
        node_1 = TextNode("This is text with a **bold** word", "text")
        node_2 = TextNode("More text with a **bold** word", "text")
        new_nodes = split_nodes_delimiter([node_1, node_2], "**", "bold")
        self.assertEqual(
            repr(new_nodes),
            '[TextNode("This is text with a ", "text"), TextNode("bold", "bold"), TextNode(" word", "text"), TextNode("More text with a ", "text"), TextNode("bold", "bold"), TextNode(" word", "text")]',
        )

    def test_uneven_delimiters(self):
        node = TextNode("This is text with *uneven delimiters", "text")
        self.assertRaises(
            ValueError, lambda: split_nodes_delimiter([node], "*", "bold")
        )

    def test_multi_links(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            "text",
        )
        new_nodes = split_nodes_link([node])
        self.assertEqual(
            repr(new_nodes),
            '[TextNode("This is text with a link ", "text"), TextNode("to boot dev", "link", "https://www.boot.dev"), TextNode(" and ", "text"), TextNode("to youtube", "link", "https://www.youtube.com/@bootdotdev")]',
        )

    def test_multi_images(self):
        node = TextNode(
            "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)",
            "text",
        )
        new_nodes = split_nodes_image([node])
        self.assertEqual(
            repr(new_nodes),
            '[TextNode("This is text with a ", "text"), TextNode("rick roll", "image", "https://i.imgur.com/aKaOqIh.gif"), TextNode(" and ", "text"), TextNode("obi wan", "image", "https://i.imgur.com/fJRm4Vk.jpeg")]',
        )

    def test_all(self):
        node = TextNode(
            "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)",
            "text",
        )
        nodes_with_bold = split_nodes_delimiter([node], "**", "bold")
        nodes_with_italic = split_nodes_delimiter(nodes_with_bold, "*", "italic")
        nodes_with_code_block = split_nodes_delimiter(nodes_with_italic, "`", "code")
        nodes_with_image = split_nodes_image(nodes_with_code_block)
        nodes_with_link = split_nodes_link(nodes_with_image)
        self.assertEqual(
            repr(nodes_with_link),
            '[TextNode("This is ", "text"), TextNode("text", "bold"), TextNode(" with an ", "text"), TextNode("italic", "italic"), TextNode(" word and a ", "text"), TextNode("code block", "code"), TextNode(" and an ", "text"), TextNode("obi wan image", "image", "https://i.imgur.com/fJRm4Vk.jpeg"), TextNode(" and a ", "text"), TextNode("link", "link", "https://boot.dev")]',
        )


if __name__ == "__main__":
    unittest.main()
