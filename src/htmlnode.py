from textnode import TextType, TextNode


class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
        
    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        string = ""
        if self.props:
            for k, v in self.props.items():
                string += f" {k}=\"{v}\""
        return string
    
    def __eq__(self, other):
        return (self.tag == other.tag
                and self.value == other.value
                and self.children == other.children
                and self.props == other.props)
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
        
    def to_html(self):
        if self.value == None:
            raise ValueError("Leaf nodes must have a value")
        elif self.tag == None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
        
    def to_html(self):
        if self.tag == None:
            raise ValueError("Parent nodes must have a tag")
        elif self.children == None:
            raise ValueError("Parent nodes must have children")
        string = ""
        for child in self.children:
            string += child.to_html()
        string = f"<{self.tag}{self.props_to_html()}>{string}</{self.tag}>"
        return string
        
    
def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            props = {}
            props["href"] = f"{text_node.url}"
            return LeafNode("a", text_node.text, props)
        case TextType.IMAGE:
            props = {}
            props["src"] = f"{text_node.url}"
            props["alt"] = f"{text_node.text}"
            return LeafNode("img", None, props)
        case _:
            raise Exception("Unknown text type")
        
