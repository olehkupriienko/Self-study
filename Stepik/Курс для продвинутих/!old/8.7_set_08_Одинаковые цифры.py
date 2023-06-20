num1 = set(int(i) for i in input())
num2 = set(int(i) for i in input())

same_digits = num1 & num2

if len(same_digits) > 0:
    print('YES')
else:
    print('NO')