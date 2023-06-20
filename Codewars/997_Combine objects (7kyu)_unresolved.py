a = {'a': 10, 'b': 20, 'c': 30}
b = {'a': 3, 'c': 6, 'd': 3}


def combine(obja, objb):  # Returns { a: 13, b: 20, c: 36, d: 3 }
    list1 = obja.items()
    list2 = objb.items()
    #set1 = set(list1.extend(list2))
    return list1


print(combine(a, b))
