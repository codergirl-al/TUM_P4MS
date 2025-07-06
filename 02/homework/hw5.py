from collections import defaultdict
import ast

text = ast.literal_eval(input())

def grpwrds(words):
    grouped = defaultdict(list)
    list(map(lambda w: grouped[len(w)].append(w), words))
    return dict(grouped)

print(grpwrds(text))