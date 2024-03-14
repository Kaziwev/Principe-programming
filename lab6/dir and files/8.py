import os

file_path = r"C:\Users\Нуртай\Downloads\githowto\githowto\repositories\work\work\lab6\delete.txt"

if os.path.exists(file_path):
    # Check if the user has permission to delete the file
    if os.access(file_path, os.W_OK):
        # Delete the file
        os.remove(file_path)
        print(f"{file_path} has been deleted.")
    else:
        print(f"ERROR: You do not have permission to delete {file_path}.")
else:
    print(f"ERROR: {file_path} does not exist.")