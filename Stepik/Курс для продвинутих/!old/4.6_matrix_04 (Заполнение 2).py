# n, m = (int(_) for _ in input().split())
n, m = (5, 5)

matrix = [[0] * m for _ in range(n)]

for j in range(m):
    for i in range(n):
        matrix[i][j] = n * j + i + 1


# print('\n'.join(' '.join((str(_).ljust(2) for _ in row)) for row in matrix))

print(*[' '.join(str(_).ljust(2) for _ in row) for row in matrix], sep="\n")