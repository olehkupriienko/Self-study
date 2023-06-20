dict1 = {'a': 100, 'z': 333, 'b': 200, 'c': 300, 'd': 45, 'e': 98, 't': 76, 'q': 34, 'f': 90, 'm': 230}
dict2 = {'a': 300, 'b': 200, 'd': 400, 't': 777, 'c': 12, 'p': 123, 'w': 111, 'z': 666}

keys1 = list(dict1.keys())
keys2 = list(dict2.keys())
all_keys = list(set(keys1 + keys2))
result = {}

for key in all_keys:
    result[key] = dict1.get(key, 0) + dict2.get(key, 0)

print(result)


