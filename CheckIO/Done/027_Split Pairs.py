test = 'abcdf'


def split_pairs(a):
    # your code here
    if len(a) % 2 != 0:
        a += '_'
    res = [a[i:i+2] for i in range(0, len(a), 2)]
    return res


print(split_pairs(test))
