s = input()
counter = s.count('f')
if counter == 1:
    print('-1')
elif counter == 0:
    print('-2')
else:
    s = s.replace('f', '_', 1)
    print(s.index('f'))
