import unittest

from src.parentnode import ParentNode
from src.leafnode import LeafNode


class TestParentNode(unittest.TestCase):
    def test_single_child_to_html(self):
        node = ParentNode("details", [LeafNode("summary", "View transcript")])
        self.assertEqual(
            node.to_html(), "<details><summary>View transcript</summary></details>"
        )

    def test_multiple_children_to_html(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_nested_parent_nodes(self):
        node = ParentNode(
            "div",
            [
                ParentNode(
                    "p",
                    [
                        LeafNode("b", "Bold text"),
                        LeafNode(None, "Normal text"),
                    ],
                ),
                ParentNode(
                    "p",
                    [
                        LeafNode("i", "italic text"),
                        LeafNode(None, "Normal text"),
                    ],
                ),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<div><p><b>Bold text</b>Normal text</p><p><i>italic text</i>Normal text</p></div>",
        )

    def test_no_tag(self):
        self.assertRaises(
            ValueError, lambda: ParentNode(children=[LeafNode(None, "Some content")])
        )

    def test_no_children(self):
        self.assertRaises(ValueError, lambda: ParentNode("div"))


if __name__ == "__main__":
    unittest.main()
