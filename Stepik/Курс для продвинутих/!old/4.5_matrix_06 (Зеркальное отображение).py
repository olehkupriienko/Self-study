n = int(input())

matrix = [[int(_) for _ in input().split()] for __ in range(n)]

mediana = len(matrix) // 2 + len(matrix) % 2
i = 0

while i < mediana:
    matrix[-i-1], matrix[i] = matrix[i], matrix[-i-1]
    i += 1

####################
# matrix.reverse() #
####################

for row in matrix:
    print(*row)
