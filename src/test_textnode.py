import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_no_url(self):
        node = TextNode("This is a text node", "normal")
        self.assertEqual(node.url, None)

    def test_eq(self):
        node_1 = TextNode("This is a text node", "bold")
        node_2 = TextNode("This is a text node", "bold")
        self.assertEqual(node_1, node_2)

    def test_repr(self):
        node = TextNode("Google", "italic", "https://google.com")
        expected_output = "TextNode(Google, italic, https://google.com)"
        self.assertEqual(repr(node), expected_output)


if __name__ == "__main__":
    unittest.main()
