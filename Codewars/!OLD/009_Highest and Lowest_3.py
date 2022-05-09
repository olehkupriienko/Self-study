numbers = "8 3 -5 42 -1 0 0 -9 4 7 4 -4"
numbers2 = []


def high_and_low(numbers):
    nn = [int(s) for s in numbers.split(" ")]
    return f'{max(nn):d} {min(nn):d}'


print(high_and_low(numbers))
