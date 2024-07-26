import unittest

from src.leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_no_props(self):
        node = LeafNode("p", "Some text")
        self.assertEqual(node.to_html(), "<p>Some text</p>")

    def test_with_props(self):
        node = LeafNode(
            tag="a",
            value="Google this",
            props={"href": "https://google.com", "target": "_blank"},
        )
        self.assertEqual(
            node.to_html(),
            '<a href="https://google.com" target="_blank">Google this</a>',
        )

    def test_repr(self):
        node = LeafNode("p", "This is a paragraph", props={"class": "lead"})
        self.assertEqual(
            repr(node), "LeafNode(p, This is a paragraph, None, {'class': 'lead'})"
        )


if __name__ == "__main__":
    unittest.main()
