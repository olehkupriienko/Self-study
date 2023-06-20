num1 = set(int(i) for i in input())
num2 = set(int(i) for i in input())

if num2.issubset(num1):
    print('YES')
else:
    print('NO')