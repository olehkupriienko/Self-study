a, b = int(input()), int(input())
max_total = 0
max_digit = 0

for i in range(a, b + 1):
    total = 0
    for j in range(1, i + 1):
        if i % j == 0:
            total = total + j
    if max_total <= total:
        max_total = total
        max_digit = i
    # print(i)
    # print('сума делителей числа', i, 'равна', total)
print(max_digit, max_total)
