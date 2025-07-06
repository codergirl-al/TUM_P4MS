usernpt = int(input())
def even_numbers(n):
	for i in range(0, n + 1, 2):
		yield i

print(','.join(str(i) for i in even_numbers(usernpt)))