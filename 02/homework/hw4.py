import re
from collections import Counter

text = input().strip()

from itertools import groupby

def top3(words):
    swords = sorted(words, key=len)
    grouped = {k: list(g) for k, g in groupby(swords, key=len)}
    return grouped


print(top3(text))

