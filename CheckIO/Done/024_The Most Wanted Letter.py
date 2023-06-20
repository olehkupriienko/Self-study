test1 = 'Hello World!'
test2 = 'How do you do?'
test3 = 'AAaooo!!!!'


def checkio(text: str) -> str:
    lst = sorted(set([i for i in text.lower() if i.isalpha()]))
    largest = 0
    for i in lst:
        if text.lower().count(i) > largest:
            largest = text.lower().count(i)
            res = i
    # return lst
    return res


print(checkio(test1))
print(checkio(test2))
print(checkio(test3))
