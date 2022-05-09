# вводяться три рядки
x, y, z = len(input()), len(input()), len(input())

M = max (x, y, z)
m = min (x, y, z)
S = x + y + z - M - m

if  (M-S) == (S-m) :
    print('YES')
else:
    print('NO')