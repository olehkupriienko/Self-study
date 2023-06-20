n = int(input())

matrix1 = [[int(_) for _ in input().split()] for __ in range(n)]

matrix2 = [[matrix1[j][i] for i in range(n)] for j in range(n)]

for row in matrix2:
    print(*row)