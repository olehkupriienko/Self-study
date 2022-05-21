test = [-2, 1, -3, 4, -1, 2, 1, -5, 4]


def maxSequence(arr):
    result_arr = []
    for i in range(len(arr)):
        for j in range(i, len(arr)+1):
            if sum(arr[i:j]) > sum(result_arr):
                result_arr = arr[i:j]
    return result_arr


print(maxSequence(test))
