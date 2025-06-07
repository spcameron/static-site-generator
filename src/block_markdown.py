from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered list"
    ORDERED_LIST = "ordered list"

def markdown_to_blocks(markdown):
    block_strings = []
    blocks = markdown.split("\n\n")
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        block_strings.append(block)
    return block_strings

def block_to_blocktype(block):
    if is_heading(block):
        return BlockType.HEADING
    elif is_code(block):
        return BlockType.CODE
    elif is_quote(block):
        return BlockType.QUOTE
    elif is_unordered_list(block):
        return BlockType.UNORDERED_LIST
    elif is_ordered_list(block):
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH

def is_heading(block):
    split_on_first_space = block.split(" ", 1)
    leading_text = split_on_first_space[0]
    
    if len(leading_text) < 1 or len(leading_text) > 6:
        return False
    
    for c in leading_text:
        if c != "#":
            return False
        
    return True

def is_code(block):
    if block[:3] != "```" or block[-3:] != "```":
        return False
    
    return True

def is_quote(block):
    lines = block.split("\n")
    for line in lines:
        if line[0] != ">":
            return False
        
    return True

def is_unordered_list(block):
    lines = block.split("\n")
    for line in lines:
        if line[0:2] != "- ":
            return False
        
    return True

def is_ordered_list(block):
    lines = block.split("\n")
    i = 1
    for line in lines:
        if line.split(" ", 1)[0] != f"{i}.":
            return False
        i += 1
        
    return True