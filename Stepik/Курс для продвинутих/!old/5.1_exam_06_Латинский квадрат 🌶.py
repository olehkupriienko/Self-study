n = int(input())

matrix = [[int(_) for _ in input().split()] for __ in range(n)]

ethalon = [i for i in range(1, n+1)]

flag = 'YES'
for i in range(n):
    row = []
    col = []
    for j in range(n):
        row.append(matrix[i][j])
        col.append(matrix[j][i])
    if sorted(row) != ethalon or sorted(col) != ethalon:
        flag = 'NO'
        break

print(flag)
