n = int(input())
max_digit = -1  # 1      n % 10
while n > 0:
    digit = n % 10
    if digit % 3 == 0:
        if digit > max_digit:  # 3      <
            max_digit = digit  # 4  max_
    n = n // 10  # 2 %
if max_digit == -1:
    print('NO')
else:
    print(max_digit)
