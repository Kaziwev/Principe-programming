import os

def list_items(path):
    print("Directories:")
    for item in os.listdir(path):
        if os.path.isdir(os.path.join(path, item)):
            print(item)

    print("\nFiles:")
    for item in os.listdir(path):
        if os.path.isfile(os.path.join(path, item)):
            print(item)

    print("\nAll directories and files:")
    for item in os.listdir(path):
        print(item)

# Specify the path
path = "."  # Current directory

# List directories, files, and all directories and files in the specified path
list_items(path)