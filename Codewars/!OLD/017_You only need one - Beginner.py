value = [66, "codewars", 11, "alex loves pushups"]
x = 66


def check(seq, elem):
    for i in seq:
        if elem == i:
            return True
    return False


def check2(seq, elem):
    return elem in seq


print(check2(value, x))