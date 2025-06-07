def extract_title(markdown):
    lines = markdown.split("\n\n")
    for line in lines:
        if line[:2] == "# ":
            return line[2:].strip()
    raise Exception("No h1 header could be found in the markdown file")

