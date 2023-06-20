n = row = col = int(input())

matrix = [[int(_) for _ in input().split()] for _ in range(n)]

matrix_trace = 0
for i in range(n):
    matrix_trace += matrix[i][i]

print(matrix_trace)
