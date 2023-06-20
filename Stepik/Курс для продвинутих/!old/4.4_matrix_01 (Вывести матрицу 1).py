n = int(input())  # numbers of row
m = int(input())  # numbers of columns

row = n
col = m

matrix = []
for i in range(row):
    temp = []
    for j in range(col):
        temp.append(input())
    matrix.append(temp)

print(*[' '.join(lst) for lst in matrix], sep='\n')

# for i in range(row):
#     for j in range(col):
#         print(matrix[i][j], end=' ')
#     print()
