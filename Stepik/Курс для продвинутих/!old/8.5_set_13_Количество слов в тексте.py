line = ''.join(i for i in input().lower() if i.isalpha() or i.isspace()).split(' ')
res = len(set(line))

print(res)
