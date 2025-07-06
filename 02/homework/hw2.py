import ast

user_input = input()

x = ast.literal_eval(user_input)

def reverse_input(x):
    return x[::-1]

print(reverse_input(x))


