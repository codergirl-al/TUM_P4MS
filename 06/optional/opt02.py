input_str = input()
binary_numbers = input_str.split(',')

div_by_5 = []

for b in binary_numbers:
    if len(b) == 4 and all(ch in '01' for ch in b):
        decimal_value = int(b, 2)
        if decimal_value % 5 == 0:
            div_by_5.append(b)

print(",".join(div_by_5))