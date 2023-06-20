password = input()

result_upper_letter = []
result_lower_letter = []
result_digit = []
result_length = len(password) >= 7
for i in password:
    result_lower_letter.append(i in password.lower() and not i.isdigit())
    result_upper_letter.append(i in password.upper() and not i.isdigit())
    result_digit.append(i.isdigit())

result2 = [any(result_upper_letter), any(result_lower_letter), any(result_digit), result_length]
print(result2)
result = all([any(result_upper_letter), any(result_lower_letter), any(result_digit), result_length])
if result:
    print('YES')
else:
    print('NO')