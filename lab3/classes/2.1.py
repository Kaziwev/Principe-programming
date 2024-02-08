class first:
    int=0 # Class attribute to store the string
    
    # Method to get the string from the user
    def get_String(k):
        k.int=int(input())
        # Method to print the string in uppercase
    def print_String(k):
        print(k.int*k.int)
        # Object creation 
obj=first()
obj.get_String()
obj.print_String()