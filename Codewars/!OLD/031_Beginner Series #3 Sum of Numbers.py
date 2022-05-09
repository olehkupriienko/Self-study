test = (-1, 0)


def get_sum(a, b):
    if a > b:
        a, b = b, a
    return a if a == b else sum([i for i in range(a, b+1)])


def get_sum2(a, b):
    return a if a == b else sum([i for i in range(min(a, b), max(a, b)+1)])