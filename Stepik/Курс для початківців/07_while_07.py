num = int(input())
flag = True
last_dig = num % 10

while num != 0:
    if last_dig != num % 10:
        flag = False
    num = num // 10

if flag:
    print('YES')
else:
    print('NO')
