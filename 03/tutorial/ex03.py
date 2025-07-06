import ast
user_input = input()
grades = ast.literal_eval(user_input)

if len(grades) == 0 or sum(grades) == 0:
	average = 0.0
else:
	average = sum(grades) / len(grades)
print(average)