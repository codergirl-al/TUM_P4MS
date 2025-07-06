import math

x = 0
y = 0

while True:
    try:
        line = input()
        if not line:
            break
        direction, steps = line.split()
        steps = int(steps)

        if direction == "UP":
            y += steps
        elif direction == "DOWN":
            y -= steps
        elif direction == "LEFT":
            x -= steps
        elif direction == "RIGHT":
            x += steps
    except:
        break

distance = math.sqrt(x**2 + y**2)
print(round(distance))
