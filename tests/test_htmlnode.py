import unittest

from src.htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_to_html(self):
        node = HTMLNode()
        self.assertRaises(NotImplementedError, node.to_html)

    def test_props_to_html(self):
        node = HTMLNode(
            props={"href": "https://example.com", "target": "_blank"},
        )
        self.assertEqual(
            node.props_to_html(), ' href="https://example.com" target="_blank"'
        )

    def test_repr(self):
        node = HTMLNode("p", "This is a paragraph", props={"class": "lead"})
        self.assertEqual(
            repr(node), "HTMLNode(p, This is a paragraph, None, {'class': 'lead'})"
        )


if __name__ == "__main__":
    unittest.main()
