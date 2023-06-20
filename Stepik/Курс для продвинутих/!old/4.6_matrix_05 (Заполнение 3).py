n = int(input())

matrix = [[1 if (i == j or n - i - 1 == j) else 0 for j in range(n)] for i in range(n)]

for row in matrix:
    for item in row:
        print(str(item).ljust(3), end='')
    print()
