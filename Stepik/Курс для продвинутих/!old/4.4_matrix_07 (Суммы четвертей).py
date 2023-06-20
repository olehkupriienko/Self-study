n = int(input())

matrix = [[int(_) for _ in input().split()] for __ in range(n)]
n1 = n2 = n3 = n4 = 0

for i in range(n):
    for j in range(n):
        if i < j and i < n - 1 - j:
            n1 += matrix[i][j]
        elif j > i > n - 1 - j:
            n2 += matrix[i][j]
        elif i > j and i > n - 1 - j:
            n3 += matrix[i][j]
        elif j < i < n - 1 - j:
            n4 += matrix[i][j]

print(f'Верхняя четверть: {n1}\nПравая четверть: {n2}\nНижняя четверть: {n3}\nЛевая четверть: {n4}')