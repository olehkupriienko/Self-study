n = int(input())

total_of_three = 0
total_of_last_digit = 0
total_even_digit = 0
total_more_five = 0
product_more_seven = 1
count_0_5_digit = 0

last_digit = n % 10

while n != 0:
    digit = n % 10
    if digit == 3:
        total_of_three += 1
    if digit == last_digit:
        total_of_last_digit += 1
    if digit % 2 == 0:
        total_even_digit += 1
    if digit > 5:
        total_more_five += digit
    if digit > 7:
        product_more_seven *= digit
    if digit == 0 or digit == 5:
        count_0_5_digit += 1
    n = n // 10
print(total_of_three, total_of_last_digit, total_even_digit, total_more_five, product_more_seven, count_0_5_digit, sep='\n')
