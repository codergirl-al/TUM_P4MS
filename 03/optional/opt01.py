text = input()
words = text.split()
freq = {}

for word in words:
    freq[word] = freq.get(word, 0) + 1

for word in sorted(freq):
    print(f"{word}:{freq[word]}")