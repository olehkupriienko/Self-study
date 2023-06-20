func = lambda x: x.lower().endswith('a') and x.lower().startswith('a')

print(func('abcd'))
print(func('bcda'))
print(func('abcda'))
print(func('Abcd'))
print(func('bcdA'))
print(func('abcdA'))
