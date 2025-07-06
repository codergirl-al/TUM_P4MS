input_str = input()

content = input_str.strip('[]').strip()

if content:
    numbers = list(map(int, content.split(',')))
else:
    numbers = []

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print(even_numbers)
