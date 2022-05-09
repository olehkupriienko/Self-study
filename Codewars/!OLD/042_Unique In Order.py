test = ''


def unique_in_order(iterable):
    if iterable == '':
        return []
    result = []
    result.append(iterable[0])
    for i in range(1, len(iterable)):
        if iterable[i] != result[-1]:
            result.append(iterable[i])
    return result


print(unique_in_order(test))
