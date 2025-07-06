def divisibl(n):
    for i in range(n + 1):
        if i % 5 == 0 and i % 7 == 0:
            yield i

n = int(input())
results = divisibl(n)
print(",".join(str(num) for num in results))
