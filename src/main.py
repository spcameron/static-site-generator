import os, shutil, sys

from copy_static import copy_files_recursive
from generate_page import generate_page_recursive


dir_path_content = "./content"
dir_path_public = "./docs"
dir_path_static = "./static"
default_basepath = "/"
html_template = "./template.html"

def main():
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:
        basepath = default_basepath
        
    print("Deleting existing docs directory ...\n")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)
        
    copy_files_recursive(dir_path_static, dir_path_public)
    generate_page_recursive(dir_path_content, html_template, dir_path_public, basepath)
    
if __name__ == "__main__":
    main()