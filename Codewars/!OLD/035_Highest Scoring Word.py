test = 'aaa b'


def high2(x):
    alfabet = 'abcdefghijklmnopqrstuvwxyz'
    result = []
    for i in x.split():
        total = 0
        for j in i:
            total += alfabet.index(j) + 1
        result.append(total)
    max_index = result.index(max(result))
    return x.split()[max_index]


def high(x):
    return max(x.split(), key=lambda k: sum(ord(c) - 96 for c in k))


print(high(test))
