entry = input()

#  i
y = 8 - int(entry[1])

#  j
x = 'abcdefgh'.index(entry[0])

matrix = [['.' for _ in range(8)] for __ in range(8)]
matrix[y][x] = 'N'

for i in range(8):
    for j in range(8):
        if (i - y)**2 + (j - x)**2 == 5:
            matrix[i][j] = '*'

for row in matrix:
    print(*row)