x = 1   # перша цифра
y = x
sum = 0
while x < 4000000:
    x, y = x + y, x
    #print(y)
    if y % 2 == 0:
        sum = sum + y

print('Сума', sum)