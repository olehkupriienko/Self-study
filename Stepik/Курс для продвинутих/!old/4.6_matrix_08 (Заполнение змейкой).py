# n, m = (int(_) for _ in input().split())
n, m = 5, 6

matrix = [[(i * m + j + 1) for j in range(m)] for i in range(n)]

for i in range(len(matrix)):
    if i % 2 == 1:
        matrix[i].reverse()




# for i in range(n):
#     for j in range(n):
#         if i <= j and i <= n - j - 1:
#             matrix[i][j] = 1
#         elif i >= j and i >= n - j - 1:
#             matrix[i][j] = 1

for row in matrix:
    print(*row)