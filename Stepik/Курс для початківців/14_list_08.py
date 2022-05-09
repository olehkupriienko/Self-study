n = int(input())
negative_digits = []
zero_digits = []
positive_digit = []
for _ in range(n):
    temp_digit = int(input())
    if temp_digit < 0:
        negative_digits.append(temp_digit)
    elif temp_digit == 0:
        zero_digits.append(temp_digit)
    else:
        positive_digit.append(temp_digit)
print(*negative_digits, *zero_digits, *positive_digit, sep='\n')
