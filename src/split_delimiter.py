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

