import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
        
    def test_different_texts(self):
        node = TextNode("This is a text node", TextType.NORMAL)
        node2 = TextNode("This is a different text node", TextType.NORMAL)
        self.assertNotEqual(node, node2)

    def test_different_text_types(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)
        
    def test_different_urls(self):
        node = TextNode("This is an image node", TextType.IMAGE, "https://google.com")
        node2 = TextNode("This is an image node", TextType.IMAGE, "https://mozilla.com")
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()