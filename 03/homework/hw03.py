input_raw = input().strip()

if input_raw.startswith('"') and input_raw.endswith('"'):
    data = input_raw[1:-1]
    seen = set()
    result = []

    for char in data:
        key = char.lower()
        if key not in seen:
            seen.add(key)
            result.append(char)

    print(''.join(result))

else:
    items = input_raw.strip('[]').split(',')
    data = []

    for item in items:
        item = item.strip().strip('"\'')
        if item.isdigit():
            data.append(int(item))
        elif item:
            data.append(item)

    seen = set()
    result = []

    for item in data:
        key = item.lower() if isinstance(item, str) else item
        if key not in seen:
            seen.add(key)
            result.append(item)

    print(''.join(map(str, result)))