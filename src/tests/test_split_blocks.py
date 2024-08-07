import unittest

from functions.block_to_block_type import block_to_block_type
from functions.markdown_to_blocks import markdown_to_blocks


class TestSplitBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        text = """# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item
"""
        blocks = markdown_to_blocks(text)
        self.assertEqual(len(blocks), 3)

    def test_excess_whitespace(self):
        text = """# This is a heading

This is a paragraph of text.
"""
        blocks = markdown_to_blocks(text)
        self.assertEqual(len(blocks), 2)

    def test_block_to_paragraph(self):
        block = "This is a paragraph"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, "paragraph")

    def test_block_to_heading(self):
        block = "# This is a heading"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, "heading")

    def test_block_to_code(self):
        block = "```This is a code block```"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, "code")

    def test_block_to_quote(self):
        block = "> This is a quote"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, "quote")

    def test_block_to_unordered_list(self):
        block = "* List item 1\n    * List item 2\n    * List item 3"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, "unordered_list")

    def test_block_to_ordered_list(self):
        block = "1. List item 1\n    2. List item 2\n    3. List item 3"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, "ordered_list")
