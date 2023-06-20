from functools import reduce


def evaluate(coefficients, x):
    n = len(coefficients)
    temp = list(zip(coefficients, list(range(n))))
    result = reduce(lambda a, b: a + b[0]*x**b[1], temp, 0)
    return result


test1 = [int(_) for _ in '2 4 3'.split()][::-1]
test2 = 10

# print(evaluate(test1, test2))
print(evaluate([int(_) for _ in input().s][::-1], int(input())))
