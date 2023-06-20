n = int(input())
trib = [1, 1, 1]

if n <= 3:
    print(*trib[:n])
else:
    for i in range(3, n):
        trib.append(sum(trib[-3:]))
    print(*trib)
