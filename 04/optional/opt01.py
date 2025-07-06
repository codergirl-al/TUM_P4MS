n = int(input())
if n == 0:
	print("0")
	exit(0)
elif n == 1:
	print("1")
	exit(0)
else:
	f = [0, 1]
	for i in range(2, n + 1):
		f.append(f[i - 1] + f[i - 2])
	print(f[n])
	exit(0)
	