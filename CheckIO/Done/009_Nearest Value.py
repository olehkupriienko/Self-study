test1 = {4, 7, 10, 11, 12, 17}
test2 = 8


def nearest_value(values: set, one: int) -> int:
    # values = sorted(values)
    # result = 0
    # delta = 10**6
    # for i in values:
    #     if abs(one - i) < delta:
    #         delta = abs(one - i)
    #         result = i
    # return result

    return min(values, key=lambda x: abs(one - x))


print(nearest_value(test1, test2))
