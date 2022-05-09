n = input().split('-')
if n[0] == '7':
    del n[0]
if [len(i) for i in n] == [3, 3, 4] and ''.join(n).isdigit():
    print('YES')
else:
    print('NO')