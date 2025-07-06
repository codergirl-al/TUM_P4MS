user_input = input("")

input_parts = user_input.split()
range_of_number = int(input_parts[0])
to_mod = int(input_parts[1])
sum_of_numbers = 0
for i in range(range_of_number + 1):
	if i % to_mod == 0:
		sum_of_numbers += i
print(sum_of_numbers)
