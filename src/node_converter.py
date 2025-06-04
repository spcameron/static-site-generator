from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode # type: ignore


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