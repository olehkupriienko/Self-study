n = int(input())

matrix = [[int(_) for _ in input().split()] for __ in range(n)]

flag = 'YES'

for i in range(n):
    for j in range(n):
        if matrix[i][j] != matrix[n-j-1][n-i-1]:
            flag = 'NO'
            break
    if flag == 'NO':
        break

print(flag)
