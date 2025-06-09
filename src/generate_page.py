import os
from pathlib import Path
from node_generator import (
    markdown_to_html_node,
)


def generate_page_recursive(from_dir_path, template_path, dest_dir_path, basepath):
    for filename in os.listdir(from_dir_path):
        from_path = os.path.join(from_dir_path, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        if os.path.isdir(from_path):
            generate_page_recursive(from_path, template_path, dest_path, basepath)
        elif os.path.isfile(from_path):
            dest_path = Path(dest_path).with_suffix(".html")
            generate_page(from_path, template_path, dest_path, basepath)
        

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path} ...\n")
    
    # md_string = ""
    with open(from_path, "r") as md_file:
        md_string = md_file.read()
        
    # html = ""
    with open(template_path, "r") as html_template:
        html = html_template.read()
    
    title = extract_title(md_string)
    md_html = markdown_to_html_node(md_string).to_html()
    
    html = html.replace("{{ Title }}", title)
    html = html.replace("{{ Content }}", md_html)
    html = html.replace("href=\"/", f"href=\"{basepath}")
    html = html.replace("src=\"/", f"src=\"{basepath}")
    
    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    with open(dest_path, "w") as file:
        file.write(html)
    
    print(f"... process complete. HTML available at {dest_path}\n")
    
def extract_title(markdown):
    lines = markdown.split("\n\n")
    for line in lines:
        if line[:2] == "# ":
            return line[2:].strip()
    raise Exception("No h1 header could be found in the markdown file")