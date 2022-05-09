test = [1, 1, 1, 1, 1, 1, 2]


def stray(arr):
    s = list(set(arr))
    a = s[0]
    b = s[1]
    a_count = arr.count(a)
    b_count = arr.count(b)
    if a_count > b_count:
        return arr[arr.index(b)]
    else:
        return arr[arr.index(a)]


print(stray(test))
