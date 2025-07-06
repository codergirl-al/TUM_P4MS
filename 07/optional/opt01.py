sentence = input()

upper_case_count = 0
lower_case_count = 0

for char in sentence:
    if char.isupper():
        upper_case_count += 1
    elif char.islower():
        lower_case_count += 1

print("UPPER CASE", upper_case_count)
print("LOWER CASE", lower_case_count)
