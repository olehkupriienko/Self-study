def add3(x):
    return x + 3


def mul7(x):
    return x * 7


def func_apply(function, items: list):
    res = []
    for item in items:
        res.append(function(item))
    return res


print(func_apply(mul7, [1, 2, 3, 4, 5, 6]))
print(func_apply(add3, [1, 2, 3, 4, 5, 6]))
print(func_apply(str, [1, 2, 3, 4, 5, 6]))
