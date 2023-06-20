n = int(input())
matrix_1 = [[int(_) for _ in input().split()] for __ in range(n)]
power = int(input())

matrix_2 = matrix_1[:]

new_matrix = [[0] * n for i in range(n)]
for x in range(power-1):
    new_matrix = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                new_matrix[i][j] += matrix_2[i][k]*matrix_1[k][j]
    matrix_2 = new_matrix[:]

for rows in new_matrix:
    print(*rows)
