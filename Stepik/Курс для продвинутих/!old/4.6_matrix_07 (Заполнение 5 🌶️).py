# n, m = (int(_) for _ in input().split())
n, m = (6, 7)

matrix = [[(i+j) % m + 1 for j in range(m)] for i in range(n)]

for row in matrix:
    print(*row)