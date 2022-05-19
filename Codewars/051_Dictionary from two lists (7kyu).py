keys = ['a', 'b', 'c', 'd']
values = [1, 2, 3]


def createDict(keys, values):
    while len(keys) > len(values):
        values.append(None)

    dictionary = dict(zip(keys, values))
    return dictionary

def createDict2(keys, values):
    return {keys[i]: values[i] if i < len(values) else None for i in range(len(keys))}


print(createDict2(keys, values))


