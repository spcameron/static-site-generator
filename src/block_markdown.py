def markdown_to_blocks(markdown):
    block_strings = []
    blocks = markdown.split("\n\n")
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        block_strings.append(block)
    return block_strings