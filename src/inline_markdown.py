import re
from textnode import TextType, TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        
        split_text = node.text.split(delimiter)
        
        if len(split_text) % 2 == 0:
            raise Exception("invalid markdown, missing a closing delimiter")
        
        curr_text_type = text_type if split_text[0] == "" else TextType.TEXT
        
        for token in split_text:
            if token == "":
                continue
            new_nodes.append(TextNode(token, curr_text_type))
            curr_text_type = text_type if curr_text_type == TextType.TEXT else TextType.TEXT
    return new_nodes

def extract_markdown_images(text):
    regex = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(regex, text)
    return matches

def extract_markdown_links(text):
    regex = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(regex, text)
    return matches

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        curr_nodes = []
        node_text = node.text
        
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        
        markdown_images = extract_markdown_images(node_text)
        
        if len(markdown_images) == 0:
            new_nodes.append(node)
            continue

        for image_alt, image_url in markdown_images:
            split_text = node_text.split(f"![{image_alt}]({image_url})", 1)
            if split_text[0] != "":
                curr_nodes.append(TextNode(split_text[0], TextType.TEXT))
            curr_nodes.append(TextNode(image_alt, TextType.IMAGE, image_url))
            node_text = split_text[1]
            
        if node_text != "":
            curr_nodes.append(TextNode(node_text, TextType.TEXT))
            
        new_nodes.extend(curr_nodes)
            
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        curr_nodes = []
        node_text = node.text
        
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        
        markdown_links = extract_markdown_links(node_text)
        
        if len(markdown_links) == 0:
            new_nodes.append(node)
            continue
        
        for link_text, link_url in markdown_links:
            split_text = node_text.split(f"[{link_text}]({link_url})")
            if split_text[0] != "":
                curr_nodes.append(TextNode(split_text[0], TextType.TEXT))
            curr_nodes.append(TextNode(link_text, TextType.LINK, link_url))
            node_text = split_text[1]
            
        if node_text != "":
            curr_nodes.append(TextNode(node_text, TextType.TEXT))
            
        new_nodes.extend(curr_nodes)
    
    return new_nodes

def text_to_text_nodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes