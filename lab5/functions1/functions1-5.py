from itertools import permutations

def print_all_permutations(input_str):
    perms = permutations(input_str)

    for perm in perms:
        print("".join(perm))

user_input = input("String: ")

print("All permutations of string:")
print_all_permutations(user_input)