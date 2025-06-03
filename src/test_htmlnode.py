import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    ### HTMLNode tests
    def test_eq(self):
        node1 = HTMLNode()
        node2 = HTMLNode()
        self.assertEqual(node1, node2)
        
    def test_props_to_html(self):
        attributes = {
            "href": "https://www.google.com", 
            "target": "_blank",
            }
        node = HTMLNode("a", "This is a link", None, attributes)
        expected = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), expected)
        
    def test_different_tags(self):
        node1 = HTMLNode("a")
        node2 = HTMLNode("p")
        self.assertNotEqual(node1, node2)
        
    ### LeafNode tests
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
        
    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_leaf_to_html_h1(self):
        node = LeafNode("h1", "My First Page")
        self.assertEqual(node.to_html(), "<h1>My First Page</h1>")
        
    def test_missing_value(self):
        node = LeafNode("p", None)
        self.assertRaises(ValueError, lambda: node.to_html())
        
    def test_missing_tag(self):
        node = LeafNode(None, "This is plain text")
        self.assertEqual(node.to_html(), "This is plain text")
        
    ### ParentNode tests
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
        
    def test_to_html_with_multiple_children(self):
        child_node = LeafNode("li", "list item")
        parent_node = ParentNode("ol", [child_node, child_node, child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<ol><li>list item</li><li>list item</li><li>list item</li></ol>"
        )
        
    def test_to_html_with_no_children(self):
        parent_node = ParentNode("div", None)
        self.assertRaises(ValueError, lambda: parent_node.to_html())
        
    def test_to_html_with_no_tag(self):
        child_node = LeafNode("p", "paragraph")
        parent_node = ParentNode(None, [child_node])
        self.assertRaises(ValueError, lambda: parent_node.to_html())

if __name__ == "__main__":
    unittest.main()