def solution(input_string: str) -> str:
	result = ""
	n = len(input_string)
	for i in range(n):
		if (i > 0 and input_string[i] == input_string[i - 1]) or (i < n - 1 and input_string[i] == input_string[i + 1]):
			continue
		result += input_string[i]
	return result

