import os, shutil

dir_path_static = "./static"
dir_path_docs = "./docs"

def copy_static_to_docs():
    print("Deleting existing public directory ...\n")
    if os.path.exists(dir_path_docs):
        shutil.rmtree(dir_path_docs)
    
    copy_files(dir_path_static, dir_path_docs)
    
def copy_files(source_dir, dest_dir):
    print(f"Calling copy function from {source_dir} to {dest_dir} ...\n")
    
    list_dir = os.listdir(source_dir)
    if list_dir:
        print(f"{source_dir} contains the following elements: {list_dir}\n")
    
    if not os.path.exists(dest_dir):
        print(f"Creating {dest_dir} directory ...\n")
        os.mkdir(dest_dir)
    
    for filename in list_dir:
        from_path = os.path.join(source_dir, filename)
        dest_path = os.path.join(dest_dir, filename)
        if os.path.isfile(from_path):
            print(f"{filename} is a file ...")
            shutil.copy(from_path, dest_path)
            print(f"... copied {filename} from {source_dir} to {dest_dir}\n")
        if os.path.isdir(from_path):
            print(f"{filename} is a directory ...\n")
            copy_files(from_path, dest_path)