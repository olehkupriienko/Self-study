# n = int(input())
n = 4

matrix = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if j == n - 1 - i:
            matrix[i][j] = 1
        elif j > n - 1 - i:
            matrix[i][j] = 2

for row in matrix:
    print(*row)