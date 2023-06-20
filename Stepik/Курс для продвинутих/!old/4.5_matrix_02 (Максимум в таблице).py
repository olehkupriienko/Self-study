n, m = int(input()), int(input())

matrix = [[int(_) for _ in input().split()] for _ in range(n)]

largest = matrix[0][0]
res = [0, 0]

for i in range(n):
    for j in range(m):
        if matrix[i][j] > largest:
            largest = matrix[i][j]
            res = [i, j]

print(*res)
