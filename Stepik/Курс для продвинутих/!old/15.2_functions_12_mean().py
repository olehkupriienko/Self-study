def mean(*args):
    result = []
    for arg in args:
        # if isinstance(arg, int | float) and not isinstance(arg, bool):
        if type(arg) in (int, float):
            result.append(arg)
    return sum(result) / len(result) if result else 0.0


print(mean())
print(mean(7))
print(mean(1.5, True, ['stepik'], 'beegeek', 2.5, (1, 2)))
print(mean(True, ['stepik'], 'beegeek', (1, 2)))
print(mean(-1, 2, 3, 10, ('5')))
print(mean(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))