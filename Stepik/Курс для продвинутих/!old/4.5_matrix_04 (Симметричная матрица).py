n = int(input())

matrix = [[int(_) for _ in input().split()] for __ in range(n)]
flag = 'YES'
for i in range(n):
    for j in range(n):
        if matrix[i][j] != matrix[j][i]:
            flag = 'NO'
            break
    if flag == 'NO':
        break

print(flag)