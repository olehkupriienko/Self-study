n,m = (int(_) for _ in input().split())

matrix = [['*' for _ in range(m)] for __ in range(n)]

for i in range(n):
    for j in range(m):
        if (i % 2 == 0 and j % 2 == 0) or (i % 2 == 1 and j % 2 == 1):
            matrix[i][j] = '.'

for rows in matrix:
    print(*rows)
