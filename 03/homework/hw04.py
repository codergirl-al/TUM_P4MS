import ast
from collections import Counter

a = ast.literal_eval(input())
b = ast.literal_eval(input())

if Counter(a) != Counter(b):
    print(False)
else:
    print(True)