test = ["a", "b", "c"]


def number(lines):
    # result = []
    # for count, item in enumerate(lines, start=1):
    #     result.append(f'{count}: {item}')
    # return result

    return [f"{count}: {item}" for count, item in enumerate(lines, start=1)]


print(number(test))
