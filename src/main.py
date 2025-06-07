import os, shutil

from copy_static import copy_static_to_public
from generate_page import generate_page

dir_path_content = "./content"
dir_path_public = "./public"
html_template = "template.html"

def main():
    copy_static_to_public()
    traverse_tree_and_generate_html(dir_path_content)
    
    
def traverse_tree_and_generate_html(source_dir):
    
    list_dir = os.listdir(source_dir)
    if list_dir:
        print(f"{source_dir} contains the following elements: {list_dir}\n")
    
    for filename in list_dir:
        source_filepath = os.path.join(source_dir, filename)
        dest_filepath = source_filepath.replace(dir_path_content, dir_path_public)
        if os.path.isdir(source_filepath):
            os.makedirs(dest_filepath, exist_ok=True)
            traverse_tree_and_generate_html(source_filepath)
        if os.path.isfile(source_filepath):
            if dest_filepath[-3:] == ".md":
                dest_filepath = dest_filepath.replace(".md", ".html")
                generate_page(source_filepath, html_template, dest_filepath)
    
if __name__ == "__main__":
    main()