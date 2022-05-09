numbers = [-1,2,3,4,-5]


def positive_sum(arr):
    return sum([i for i in arr if i > 0]) if arr else 0


print(positive_sum(numbers))
