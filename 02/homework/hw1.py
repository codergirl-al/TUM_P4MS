user_input = input().strip('\"')

letters = []

for char in user_input:
	if (char.isalpha()):
		if char.isupper():
			letters.append(ord(char) - 64)
		else:
			letters.append(ord(char) - 97 + 1)

print(letters)



# whatever

user_input = input()
letters = [ord(char.lower()) - 97 + 1 for char in user_input if char.isalpha()]
print(letters)


user_input = input()
letters = [0] * len(user_input)

for i in range(len(user_input)):
    letters[i] = ord(user_input[i]) - 97 + 1

print(letters)