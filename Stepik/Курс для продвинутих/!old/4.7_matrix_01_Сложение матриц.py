n, m = (int(_) for _ in input().split())

matrix1 = [[int(_) for _ in input().split()] for __ in range(n)]
input()
# x = input()
matrix2 = [[int(_) for _ in input().split()] for ___ in range(n)]

print(matrix1)
print()
print(matrix2)

matrix3 = [[matrix1[i][j]+matrix2[i][j] for j in range(m)] for i in range(n)]

for rows in matrix3:
    print(*rows)