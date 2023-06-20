n = int(input())

matrix = [[int(_) for _ in input().split()] for __ in range(n)]

largest = matrix[0][0]

for i in range(n):
    for j in range(n):
        if (j <= i <= (n - 1 - j)) or (j >= i >= (n - 1 - j)):
            if largest < matrix[i][j]:
                largest = matrix[i][j]

print(largest)