def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

arr_input = input().strip()
target_input = input().strip()

if arr_input == '[]' or arr_input.strip() == '':
    arr = []
else:
    arr = list(map(int, arr_input.strip('[]').split(',')))

target = int(target_input)
print(binary_search(arr, target))