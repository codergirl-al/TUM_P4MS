nbr = int(input())

def putNumbers(n):
	for i in range(n, -1, -1):
		if i % 7 == 0:
			yield i

print(list(putNumbers(nbr)))
