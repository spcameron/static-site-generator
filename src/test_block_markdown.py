import unittest
from block_markdown import (
    BlockType,
    markdown_to_blocks,
    block_to_blocktype,
)

class TestBlockMarkdown(unittest.TestCase):
    ### markdown to block tests
    def test_markdown_to_block(self):
        md = """
This is a paragraph **written in bold** text.

This is another paragraph with _italic text_ and `inline code.`

- This is a list
- with only two items
        """
        blocks = markdown_to_blocks(md)
        self.assertListEqual(
            [
                "This is a paragraph **written in bold** text.",
                "This is another paragraph with _italic text_ and `inline code.`",
                "- This is a list\n- with only two items"
            ],
            blocks,
        )
        
    ### block to blocktype tests
    def test_paragraph_block(self):
        block = "This is a normal paragraph block"
        expected = BlockType.PARAGRAPH
        self.assertEqual(block_to_blocktype(block), expected)

    def test_heading_block_h1(self):
        block = "# This is an h1 block"
        expected = BlockType.HEADING
        self.assertEqual(block_to_blocktype(block), expected)
        
    def test_heading_block_h6(self):
        block = "###### This is an h6 block"
        expected = BlockType.HEADING
        self.assertEqual(block_to_blocktype(block), expected)
        
    def test_code_block(self):
        block = "```This is a code block```"
        expected = BlockType.CODE
        self.assertEqual(block_to_blocktype(block), expected)
        
    def test_quote_block(self):
        block = "> This is a quote\n> This is the second line of a quote"
        expected = BlockType.QUOTE
        self.assertEqual(block_to_blocktype(block), expected)

    def test_unordered_list(self):
        block = "- This is an unordered list\n- This is the second line"
        expected = BlockType.UNORDERED_LIST
        self.assertEqual(block_to_blocktype(block), expected)
        
    def test_ordered_list(self):
        block = "1. This is an ordered list\n2. This is the second line"
        expected = BlockType.ORDERED_LIST
        self.assertEqual(block_to_blocktype(block), expected)