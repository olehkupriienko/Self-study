n = 25

def is_square(n):
    return int(n ** 0.5) ** 2 == n


def is_square2(n):
    return (n ** 0.5).is_integer()

print(is_square2(n))
