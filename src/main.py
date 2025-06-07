import os
import shutil

def main():
    if os.path.exists("./public/"):
        shutil.rmtree("./public/")
        print("Deleted existing public directory")
    os.mkdir("./public/")
    print("Created new public directory")
    
    copy_tree("./static/", "./public/")
    
def copy_tree(source_dir, target_dir):
    print(f"Calling copy function from {source_dir} to {target_dir}")
    
    list_dir = os.listdir(source_dir)
    print(f"{source_dir} contains the following elements")
    print(list_dir)
    
    for item in list_dir:
        curr_path = os.path.join(source_dir, item)
        target_path = os.path.join(target_dir, item)
        if os.path.isfile(curr_path):
            print(f"{item} is a file")
            shutil.copy(curr_path, target_path)
            print(f"Copied {item} from {source_dir} to {target_dir}")
        if os.path.isdir(curr_path):
            print(f"{item} is a dir")
            if not os.path.exists(target_path):
                os.mkdir(target_path)
                print(f"Created {target_path}")
            copy_tree(curr_path, target_path)
    

if __name__ == "__main__":
    main()