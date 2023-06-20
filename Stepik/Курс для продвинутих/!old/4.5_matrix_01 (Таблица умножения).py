row, col = int(input()), int(input())

mult = [[i * j for j in range(col)] for i in range(row)]

for lists in mult:
    print(*list(str(items).ljust(2) for items in lists))
