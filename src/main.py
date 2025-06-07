import os, shutil

from copy_static import copy_static_to_public
from generate_page import generate_page

dir_path_content = "./content"
dir_path_public = "./public"
html_template = "template.html"

def main():
    copy_static_to_public()
    traverse_tree_and_copy(dir_path_content)
    
    
def traverse_tree_and_copy(source_dir):
    list_dir = os.listdir(source_dir)
    
    for filename in list_dir:
        source_filepath = os.path.join(source_dir, filename)
        if os.path.isdir(source_filepath):
            dest_filepath = source_filepath.replace(dir_path_content, dir_path_public)
            os.mkdir(dest_filepath)
            traverse_tree_and_copy(source_filepath)
        if os.path.isfile(source_filepath):
            dest_filepath = source_filepath.replace(dir_path_content, dir_path_public).replace(".md", ".html")
            generate_page(source_filepath, html_template, dest_filepath)
    
if __name__ == "__main__":
    main()