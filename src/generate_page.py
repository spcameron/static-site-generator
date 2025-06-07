import os
from node_generator import (
    markdown_to_html_node,
)

def extract_title(markdown):
    lines = markdown.split("\n\n")
    for line in lines:
        if line[:2] == "# ":
            return line[2:].strip()
    raise Exception("No h1 header could be found in the markdown file")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path} ...\n")
    
    md_string = ""
    with open(from_path) as md_file:
        md_string = md_file.read()
        
    html = ""
    with open(template_path) as html_template:
        html = html_template.read()
    
    title = extract_title(md_string)
    md_html = markdown_to_html_node(md_string).to_html()
    
    html = html.replace("{{ Title }}", title)
    html = html.replace("{{ Content }}", md_html)
    
    with open(dest_path, "w") as file:
        file.write(html)
    
    print(f"Process complete. HTML available at {dest_path}")