test = [2, 3, 4, 1]


def replace_last(line: list) -> list:
    if line:
        line.insert(0, line.pop(-1))
    return line


print(replace_last(test))
