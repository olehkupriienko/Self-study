n = int(input())

matrix = [[int(_) for _ in input().split()] for __ in range(n)]

new_matrix = [[matrix[-i-1][j] for i in range(n)] for j in range(n)]

# new_matrix = []
#
# for j in range(n):
#     temp = []
#     for i in range(n):
#         temp.append(matrix[-i-1][j])
#     new_matrix.append(temp)


for row in new_matrix:
    print(*row)
