test = "Hi!!!"


def remove(s: str):
    s = s.rstrip('!')
    return s


print(remove(test))
