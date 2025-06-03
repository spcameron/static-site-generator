import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node1, node2)
        
    def test_different_texts(self):
        node1 = TextNode("This is a text node", TextType.NORMAL)
        node2 = TextNode("This is a different text node", TextType.NORMAL)
        self.assertNotEqual(node1, node2)

    def test_different_text_types(self):
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node1, node2)
        
    def test_different_urls(self):
        node1 = TextNode("This is an image node", TextType.IMAGE, "https://google.com")
        node2 = TextNode("This is an image node", TextType.IMAGE, "https://mozilla.com")
        self.assertNotEqual(node1, node2)

if __name__ == "__main__":
    unittest.main()