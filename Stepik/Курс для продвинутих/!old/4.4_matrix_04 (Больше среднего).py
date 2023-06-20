n = int(input())

matrix = [[int(_) for _ in input().split()] for _ in range(n)]

for row in matrix:
    print(len(list(filter(lambda a: a > sum(row)/len(row), row))))
    