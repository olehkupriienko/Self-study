n = int(input())

for i in range(1, int(n/2)+1):
    for j in range(i):
        print('*', end='')
    print()

for i in range(int(n/2)+1, 0, -1):
    for j in range(i, 0, -1):
        print('*', end='')
    print()
