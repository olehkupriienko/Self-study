m = int(input())
n = int(input())

books = {input() for _ in range(m)}

for _ in range(n):
    if input() in books:
        print('YES')
    else:
        print('NO')
