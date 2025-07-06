user_input = input("")
input_parts = user_input.split()
n = int(input_parts[0])
steps = 0
while n != 1:
	if n % 2 == 0:
		n = n // 2
	else:
		n = 3 * n + 1
	steps += 1
print(steps)