import re

from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode
from inline_markdown import (
    text_to_text_nodes,
)
from block_markdown import (
    markdown_to_blocks,
    block_to_blocktype,
    BlockType,
)


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
            return LeafNode("a", text_node.text, {"href": text_node.url})
        case TextType.IMAGE:
            return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
        case _:
            raise Exception("Unknown text type")
        
def markdown_to_html_node(markdown):
    block_nodes = []
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        block_tag = block_to_block_tag(block)
        block_children = text_to_children(block)
        if block_tag == "code":
            block_node = ParentNode("pre", block_children)
        else:
            block_node = ParentNode(block_tag, block_children)
        block_nodes.append(block_node)
    return ParentNode("div", block_nodes)
    
def block_to_block_tag(block):
    block_type = block_to_blocktype(block)
    match block_type:
        case BlockType.HEADING:
            split_on_first_space = block.split(" ", 1)
            heading_size = len(split_on_first_space[0])
            return f"h{heading_size}"
        case BlockType.CODE:
            return "code"
        case BlockType.QUOTE:
            return "blockquote"
        case BlockType.UNORDERED_LIST:
            return "ul"
        case BlockType.ORDERED_LIST:
            return "ol"
        case BlockType.PARAGRAPH:
            return "p"
        case _:
            raise Exception("Unknown BlockType")
   
def text_to_children(block):
    children = []
    block_type = block_to_blocktype(block)
    match block_type:
        case BlockType.HEADING:
            children.extend(heading_text_to_children(block))
        case BlockType.CODE:
            children.extend(code_text_to_children(block))
        case BlockType.QUOTE:
            children.extend(quote_text_to_children(block))
        case BlockType.UNORDERED_LIST:
            children.extend(ul_text_to_children(block))
        case BlockType.ORDERED_LIST:
            children.extend(ol_text_to_children(block))
        case BlockType.PARAGRAPH:
            children.extend(paragraph_text_to_children(block))
        case _:
            raise Exception("Unknown BlockType")
    return children

def paragraph_text_to_children(block):
    html_nodes = []
    text_nodes = text_to_text_nodes(block.replace("\n", " "))
    for node in text_nodes:
        html_node = text_node_to_html_node(node)
        html_nodes.append(html_node)
    return html_nodes

def heading_text_to_children(block):
    html_nodes = []
    split_on_first_space = block.split(" ", 1)
    block_text = split_on_first_space[1]
    text_nodes = text_to_text_nodes(block_text)
    for node in text_nodes:
        html_node = text_node_to_html_node(node)
        html_nodes.append(html_node)
    return html_nodes

def code_text_to_children(block):
    block_text = block[3:-3]
    text_node = TextNode(block_text, TextType.CODE)
    html_node = text_node_to_html_node(text_node)
    return [html_node]

def quote_text_to_children(block):
    html_nodes = []
    split_lines = block.split(">")
    for line in split_lines:
        text_nodes = text_to_text_nodes(line.replace("\n", " ").lstrip())
        for node in text_nodes:
            html_node = text_node_to_html_node(node)
            html_nodes.append(html_node)
    return html_nodes

def ul_text_to_children(block):
    html_nodes = []
    split_lines = block.split("- ")
    for line in split_lines:
        text_nodes = text_to_text_nodes(line.rstrip())
        for node in text_nodes:
            html_nodes.append(generate_list_item_node(node))
    return html_nodes

def ol_text_to_children(block):
    html_nodes = []
    split_lines = split_ordered_list(block)
    for line in split_lines:
        text_nodes = text_to_text_nodes(line.rstrip())
        for node in text_nodes:
            html_nodes.append(generate_list_item_node(node))
    return html_nodes

def split_ordered_list(block):
    regex = r"([0-9]+\. )"
    matches = re.findall(regex, block)
    block_text = block
    split_lines = []
    for match in matches:
        split_text = block_text.split(match, 1)
        line = split_text[0]
        split_lines.append(line)
        block_text = split_text[1]
    split_lines.append(block_text)
    return split_lines

def generate_list_item_node(text_node):
    list_item_children = []
    html_node = text_node_to_html_node(text_node)
    list_item_children.append(html_node)
    list_item_node = ParentNode("li", list_item_children)
    return list_item_node