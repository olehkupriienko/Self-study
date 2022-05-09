m, p, n = int(input()), int(input()), int(input())
print('1', m)
for i in range(n - 1):
    m = m + m * p / 100
    print(i + 2, m)
