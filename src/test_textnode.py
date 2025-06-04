import unittest

from textnode import TextNode, TextType
from split_delimiter import split_nodes_delimiter


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node1, node2)
        
    def test_different_texts(self):
        node1 = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a different text node", TextType.TEXT)
        self.assertNotEqual(node1, node2)

    def test_different_text_types(self):
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node1, node2)
        
    def test_different_urls(self):
        node1 = TextNode("This is an image node", TextType.IMAGE, "https://google.com")
        node2 = TextNode("This is an image node", TextType.IMAGE, "https://mozilla.com")
        self.assertNotEqual(node1, node2)
        
    ### delimiter tests
    def test_inline_code_block(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected)
        
    def test_begins_with_code_block(self):
        node = TextNode("`A code block` starts this text", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [
            TextNode("A code block", TextType.CODE),
            TextNode(" starts this text", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected)
        
    def test_ends_with_code_block(self):
        node = TextNode("This text ends with `a code block`", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [
            TextNode("This text ends with ", TextType.TEXT),
            TextNode("a code block", TextType.CODE),
        ]
        self.assertEqual(new_nodes, expected)
        
    def test_contains_multiple_code_blocks(self):
        node = TextNode("This text has `one code block` and `another code block`", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [
            TextNode("This text has ", TextType.TEXT),
            TextNode("one code block", TextType.CODE),
            TextNode(" and ", TextType.TEXT),
            TextNode("another code block", TextType.CODE),
        ]
        self.assertEqual(new_nodes, expected)
        
    def test_contains_consecutive_code_blocks(self):
        node = TextNode("This text contains `two consecutive` `code blocks`", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [
            TextNode("This text contains ", TextType.TEXT),
            TextNode("two consecutive", TextType.CODE),
            TextNode(" ", TextType.TEXT),
            TextNode("code blocks", TextType.CODE),
        ]
        self.assertEqual(new_nodes, expected)

if __name__ == "__main__":
    unittest.main()