n = int(input())

matrix = [[int(_) for _ in input().split()] for __ in range(n)]


new_mat = [matrix[i][j] if i >= n - 1 - j else None for i in range(n) for j in range(n)]

print(max(new_mat))

# largest =
# for i in range(n):
#     for j in range(n):

