test = '2BclkH5MRqLRFemzuZK1GKJ2UmQn6CRBHMKb6TDc37sLyl'


def duplicate_count(text):
    result = list(text.lower())
    count = 0
    while len(result) != 0:
        a = result[0]
        if result.count(a) > 1:
            count += 1
        while a in result:
            result.remove(a)
    return count


def duplicate_count2(text):
    return len([c for c in set(text.lower()) if text.lower().count(c) > 1])


print(duplicate_count2(test))
