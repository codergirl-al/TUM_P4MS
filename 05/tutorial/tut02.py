from solution import solution

input_str = input()
input_list = [int(x.strip()) for x in input_str.split(",")]

if solution(input_list):
	print("True")
else:
	print("False")