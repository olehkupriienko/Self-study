test1 = [(45, 12), (55, 21), (19, -2), (104, 20)]


def open_or_senior(data):
    result = []
    for pairs in data:
        age, handicap = pairs
        if age >= 55 and handicap >= 7:
            result.append('Senior')
        else:
            result.append('Open')
    return result

    # return ["Senior" if age >= 55 and handicap >= 8 else "Open" for (age, handicap) in data]



print(open_or_senior(test1))
