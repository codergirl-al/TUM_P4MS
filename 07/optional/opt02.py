net_amount = 0

while True:
    try:
        line = input()
        if not line:
            break
        parts = line.split()
        if len(parts) != 2:
            continue
        operation, amount_str = parts
        amount = int(amount_str)
        if operation.upper() == 'D':
            net_amount += amount
        elif operation.upper() == 'W':
            net_amount -= amount
    except:
        break

print(net_amount)
