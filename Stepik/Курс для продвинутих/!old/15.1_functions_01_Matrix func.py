def matrix(i=1, j=None, x=0):
    if j is None:
        j = i
    matrix_result = []
    for _ in range(i):
        matrix_result.append([x] * j)
    return matrix_result


print(matrix())
print(matrix(3))
print(matrix(2, 5))
print(matrix(3, 4, 9))