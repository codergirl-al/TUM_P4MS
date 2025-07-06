import math

C = 50
H = 30
inpt = input()
Dvals = inpt.split(',')
Qvals = []

for d in Dvals:
    D = int(d)
    Q = math.sqrt((2 * C * D) / H)
    Qvals.append(str(round(Q)))

print(",".join(Qvals))