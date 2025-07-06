user_input = input()

age, base_fare = map(int, user_input.split())

if age <= 5:
	final = 0
elif 6 <= age <= 18:
	final = base_fare * 0.5
elif 19 <= age <= 60:
	final = base_fare
else:
	final = base_fare * 0.75
print(final)