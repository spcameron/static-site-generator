import unittest

from textnode import TextNode, TextType
from node_generator import (
    text_node_to_html_node,
    markdown_to_html_node,
    block_to_block_tag
)


class TestHTMLNode(unittest.TestCase):
    ### generating html tests
    def test_h1_html(self):
        md = "# This is an h1 block"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html, "<div><h1>This is an h1 block</h1></div>")
        
    def test_h1_and_h2_html(self):
        md = "# This is an h1 block\n\n## This is an h2 block"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html, "<div><h1>This is an h1 block</h1><h2>This is an h2 block</h2></div>")
        
    def test_p_html(self):
        md = "This is a paragraph element with some **bold text** and some _italic text_"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html, "<div><p>This is a paragraph element with some <b>bold text</b> and some <i>italic text</i></p></div>")
        
    def test_multiple_p_html(self):
        md = "This is a paragraph\n\nThis is another paragraph"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html, "<div><p>This is a paragraph</p><p>This is another paragraph</p></div>")

    def test_p_with_linebreaks(self):
        md = "This is\na paragraph\nwith linebreaks"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html, "<div><p>This is a paragraph with linebreaks</p></div>")

    def test_code_html(self):
        md = "```This is code that _should_ remain\nthe **same** even with inline stuff```"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html, "<div><pre><code>This is code that _should_ remain\nthe **same** even with inline stuff</code></pre></div>")
        
    def test_quote_html(self):
        md = ">This is a one line quote"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html, "<div><blockquote>This is a one line quote</blockquote></div>")
        
    def test_multiline_quote_html(self):
        md = ">This is a quote\n>With two lines"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html, "<div><blockquote>This is a quote\nWith two lines</blockquote></div>")
        
    def test_unordered_list_html(self):
        md = "- A list item\n- Another list item\n- One more list item"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html, "<div><ul><li>A list item</li><li>Another list item</li><li>One more list item</li></ul></div>")
        
    def test_ordered_list_html(self):
        md = "1. The first item\n2. The second item\n3. The third item"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html, "<div><ol><li>The first item</li><li>The second item</li><li>The third item</li></ol></div>")

    ### block_tag tests
    def test_h1_tag(self):
        block = "# This is an h1 block"
        block_tag = block_to_block_tag(block)
        self.assertEqual(block_tag, "h1")
    
    def test_h6_tag(self):
        block = "###### This is an h6 block"
        block_tag = block_to_block_tag(block)
        self.assertEqual(block_tag, "h6")
        
    def test_code_tag(self):
        block = "```This is a code block```"
        block_tag = block_to_block_tag(block)
        self.assertEqual(block_tag, "code")
        
    def test_quote_tag(self):
        block = "> This is a quote\n> This is still a quote"
        block_tag = block_to_block_tag(block)
        self.assertEqual(block_tag, "blockquote")

    def test_ul_tag(self):
        block = "- This is an unordered list\n- This is the second item"
        block_tag = block_to_block_tag(block)
        self.assertEqual(block_tag, "ul")

    def test_ol_tag(self):
        block = "1. This is an ordered list\n2. this is the second item"
        block_tag = block_to_block_tag(block)
        self.assertEqual(block_tag, "ol")
        
    ### TextNode to HTMLNode tests
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
        
    def test_bold(self):
        node = TextNode("This is a bold text node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold text node")
        
    def test_italic(self):
        node = TextNode("This is an italic text node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is an italic text node")
        
    def test_code(self):
        node = TextNode("This is a code node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a code node")

    def test_link(self):
       node = TextNode("This is a link node", TextType.LINK, "https://google.com") 
       html_node = text_node_to_html_node(node)
       self.assertEqual(html_node.tag, "a")
       self.assertEqual(html_node.value, "This is a link node")
       self.assertEqual(
           html_node.props,
           {
               "href": "https://google.com"
           })
       
    def test_img(self):
        node = TextNode("This is an image node", TextType.IMAGE, "./assets/cat_dog.png")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, None)
        self.assertEqual(
            html_node.props,
            {
                "src": "./assets/cat_dog.png",
                "alt": "This is an image node"
            }
        )