n = int(input())

matrix = [[int(_) for _ in input().split()] for __ in range(n)]

for i in range(n):
    matrix[i][i], matrix[-i-1][i] = matrix[-i-1][i], matrix[i][i]

for row in matrix:
    print(*row)