test1 = [1, 2, 3]
test2 = [1, 2]


def array_diff(a, b):

    # c = []
    # for i in a:
    #     if i not in b:
    #         c.append(i)
    # return c

    return [item for item in a if item not in b]


print(array_diff(test1, test2))
