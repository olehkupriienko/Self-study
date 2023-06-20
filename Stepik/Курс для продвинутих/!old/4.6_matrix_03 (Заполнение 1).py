# n = int(input())
n = 3
# m = int(input())
m = 5

matrix = [[0 for _ in range(m)] for __ in range(n)]

counter = 1
for i in range(n):
    for j in range(m):
        matrix[i][j] = counter
        counter += 1

for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(2), end=' ')
    print()

# print('\n'.join(' '.join((str(_).ljust(2) for _ in lst)) for lst in matrix))
