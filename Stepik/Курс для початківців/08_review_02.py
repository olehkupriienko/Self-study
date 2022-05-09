mx = -10**6
s = 0
for i in range(10):      # помилка 2
    x = int(input())
    if x < 0:
        s += x      # помилка 1
        if x > mx:
            mx = x
if s != 0:
    print(s)
    print(mx)
else:
    print('NO')
