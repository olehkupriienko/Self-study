n1, m1 = (int(_) for _ in input().split())
matrix1 = [[int(_) for _ in input().split()] for __ in range(n1)]
input()
# x = input()
n2, m2 = (int(_) for _ in input().split())
matrix2 = [[int(_) for _ in input().split()] for ___ in range(n2)]

matrix3 = [[0] * m2 for i in range(n1)]

for i in range(n1):
    for j in range(m2):
        for k in range(n2):
            matrix3[i][j] += matrix1[i][k]*matrix2[k][j]



for rows in matrix3:
    print(*rows)