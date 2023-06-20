# n = int(input())
n = 5
matrix = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i <= j and i <= n - j -1:
            matrix[i][j] = 1
        elif i >= j and i >= n - j - 1:
            matrix[i][j] = 1
for row in matrix:
    print(*row)