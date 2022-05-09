def binary_array_to_number(arr):
    result = ''
    for i in arr:
        result += str(i)
    return int(result, 2)


def binary_array_to_number2(arr):
    return int("".join(map(str, arr)), 2)


print(binary_array_to_number2([1, 1, 1, 1]))
