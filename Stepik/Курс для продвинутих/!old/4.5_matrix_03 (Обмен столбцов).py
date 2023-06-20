n = row = int(input())
m = col = int(input())

matrix = [[int(_) for _ in input().split()] for __ in range(row)]

i, j = (int(_) for _ in input().split())

for _ in range(row):
    matrix[_][i], matrix[_][j] = matrix[_][j], matrix[_][i]

for _ in range(row):
    for __ in range(col):
        print(matrix[_][__], end=' ')
    print()