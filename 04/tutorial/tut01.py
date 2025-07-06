import ast
input_string = input("")
numbers = ast.literal_eval(input_string)
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)