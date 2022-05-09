flag = 'ДА'
for num in input().split('.'):
    if int(num) < 0 or int(num) > 255:
        flag = 'НЕТ'
        break
print(flag)
