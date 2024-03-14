import string

# Loop through each uppercase letter
for letter in string.ascii_uppercase:  
    # Create the filename
    filename = letter + ".txt"
    # Open the file and write the message
    with open(filename, "w") as file:
        file.write("This is file " + filename)