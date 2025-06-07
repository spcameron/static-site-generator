from copy_static import copy_static_to_public
from generate_page import generate_page

path_from = "content/index.md"
path_template = "template.html"
path_dest = "public/index.html"

def main():
    copy_static_to_public()
    generate_page(path_from, path_template, path_dest)
    
if __name__ == "__main__":
    main()