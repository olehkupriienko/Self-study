from functools import reduce


def digits_multiplication(number: int) -> int:
    # digits = [int(x) if x != '0' else 1 for x in str(number)]
    multiplication = reduce(lambda x, y: x * y, [int(a) if a != '0' else 1 for a in str(number)], 1)
    return multiplication



print(digits_multiplication(123405) == 120)
print(digits_multiplication(999) == 729)
print(digits_multiplication(1000) == 1)
print(digits_multiplication(1111) == 1)