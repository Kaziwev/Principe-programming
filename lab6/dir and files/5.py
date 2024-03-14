my_list = ["apple", "banana", "cherry", "date"]

# Open a file in write mode
with open("list.txt", "w") as file:  
    for item in my_list:
        file.write(item + "\n")  