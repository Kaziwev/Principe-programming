import os

path = r"C:\Users\Нуртай\Downloads"  #Downloads is a directory that contains files and possibly other directories.

if os.path.exists(path):
    print("Path exists")
    directory, filename = os.path.split(path)
    print("Directory:", directory)
    print("Filename:", filename)
else:
    print("Path does not exist")
