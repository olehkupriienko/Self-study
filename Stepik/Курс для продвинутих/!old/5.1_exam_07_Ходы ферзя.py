matrix = [['.' for _ in range(8)] for __ in range(8)]

ij = input()
i_f = 8-int(ij[1])
j_f = 'abcdefgh'.index(ij[0])

for i in range(8):
    for j in range(8):
        if i == i_f or j == j_f or abs(i_f - i) == abs(j_f - j):
            matrix[i][j] = '*'

matrix[i_f][j_f] = 'Q'

for row in matrix:
    print(*row)
