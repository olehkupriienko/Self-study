num = int(input())
flag = 'YES'
digit = 0

while num >= 10:
    if (num % 10) > ((num % 100) // 10):
        flag = 'NO'
    num = num // 10

print(flag)
