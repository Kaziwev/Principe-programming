from itertools import permutations
def permutation():
    s = input("String : ")
    perms = permutations(s) 
    
    print("All permutations : ")
    for perm in perms:
        print(''.join(perm))
permutation()