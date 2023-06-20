# test1 = [0, 1, 2, 3, 4, 5]
# test1 = [6]
test1 = []


def checkio(array: list) -> int:
    """
        sums even-indexes elements and multiply at the last
    """
    total = sum([array[i] for i in range(0, len(array), 2)])
    return 0 if not array else total*array[-1]


print(checkio(test1))
