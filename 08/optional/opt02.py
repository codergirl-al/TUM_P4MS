input_str = input()

content = input_str.strip('[]').strip()
numbers = list(map(int, content.split(','))) if content else []

result = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, numbers)))


print(result)
