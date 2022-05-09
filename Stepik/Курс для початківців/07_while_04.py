dig = int(input())
largest_dig = 0
smallest_dig = 9

while dig !=0:
    last_dig = dig % 10
    if largest_dig <= last_dig:
        largest_dig = last_dig
    if smallest_dig >= last_dig:
        smallest_dig = last_dig
    dig = dig // 10

print('Максимальная цифра равна', largest_dig)
print('Минимальная цифра равна', smallest_dig)
