
source_file = "source.txt"

# Destination file path
destination_file = "destination.txt"

# Open the source file in read mode and the destination file in write mode
with open(source_file, "r") as source, open(destination_file, "w") as destination:
    # Read the contents of the source file
    contents = source.read()
    # Write the contents to the destination file
    destination.write(contents)

print("File copied successfully.")