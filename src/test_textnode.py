import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("Google", "italic", "https://google.com")
        expected_repr = "TextNode(Google, italic, https://google.com)"
        self.assertEqual(str(node), expected_repr)

    def test_no_url(self):
        node = TextNode("This is a text node", "normal")
        self.assertEqual(node.url, None)


if __name__ == "__main__":
    unittest.main()
