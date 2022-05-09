temp = [6, 2, 1, 8, 10]


def sum_array(arr):
    return 0 if (arr is None or len(arr) < 3) else sum(arr) - min(arr) - max(arr)


print(sum_array(temp))
