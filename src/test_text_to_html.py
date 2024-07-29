import unittest

from textnode import TextNode
from utils import text_node_to_html_node


class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        text_node = TextNode("Regular text", "text")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(repr(html_node), "LeafNode(None, Regular text, None)")

    def test_bold(self):
        text_node = TextNode("Bold text", "bold")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(repr(html_node), "LeafNode(b, Bold text, None)")

    def test_italic(self):
        text_node = TextNode("Italic text", "italic")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(repr(html_node), "LeafNode(i, Italic text, None)")

    def test_code(self):
        text_node = TextNode("Code text", "code")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(repr(html_node), "LeafNode(code, Code text, None)")

    def test_link(self):
        text_node = TextNode("Link text", "link", "https://google.com")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(
            repr(html_node), "LeafNode(a, Link text, {'href': 'https://google.com'})"
        )

    def test_image(self):
        text_node = TextNode("Image alt text", "image", "/assets/image.jpg")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(
            repr(html_node),
            "LeafNode(img, , {'src': '/assets/image.jpg', 'alt': 'Image alt text'})",
        )


if __name__ == "__main__":
    unittest.main()
