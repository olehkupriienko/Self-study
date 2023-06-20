n = int(input())

matrix = [[int(_) for _ in input().split()] for __ in range(n)]

largest = matrix[0][0]

for i in range(n):
    for j in range(i+1):
        if matrix[i][j] > largest:
            largest = matrix[i][j]

print(largest)