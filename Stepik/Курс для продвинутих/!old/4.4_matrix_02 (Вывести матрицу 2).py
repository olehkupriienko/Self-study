row = int(input())  # numbers of row
col = int(input())  # numbers of columns

matrix = [[input() for j in range(col)] for i in range(row)]

# for i in range(row):
#     matrix.append([input() for j in range(col)])

for i in range(row):
    for j in range(col):
        print(matrix[i][j], end=' ')
    print()
print()

for j in range(col):
    for i in range(row):
        print(matrix[i][j], end=' ')
    print()
