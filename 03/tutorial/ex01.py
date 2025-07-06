first_input = input()
second_input = input()

x, a = map(int, first_input.split())
y, b = map(int, second_input.split())

if a == b:
    print("Undeterminable")
else:
    sustainable_population = round((x * a - y * b) / (a - b), 2)
    print("%.2f" % sustainable_population)