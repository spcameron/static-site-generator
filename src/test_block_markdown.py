import unittest
from block_markdown import (
    markdown_to_blocks
)

class TestBlockMarkdown(unittest.TestCase):
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