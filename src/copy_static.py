import os, shutil

    
def copy_files_recursive(source_dir, dest_dir):
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
        elif os.path.isdir(from_path):
            copy_files_recursive(from_path, dest_path)