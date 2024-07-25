import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_to_html(self):
        node = HTMLNode()
        self.assertRaises(NotImplementedError, node.to_html)

    def test_props_to_html(self):
        node = HTMLNode(
            props={"href": "https://example.com", "target": "_blank"},
        )
        expected_output = ' href="https://example.com" target="_blank"'
        self.assertEqual(node.props_to_html(), expected_output)

    def test_repr(self):
        node = HTMLNode("p", "This is a paragraph", props={"class": "lead"})
        expected_output = "HTMLNode(p, This is a paragraph, None, {'class': 'lead'})"
        self.assertEqual(repr(node), expected_output)


if __name__ == "__main__":
    unittest.main()
