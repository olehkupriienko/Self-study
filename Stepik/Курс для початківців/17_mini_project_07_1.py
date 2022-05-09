base = 2
old_digit = 513

new_digit = ''

while old_digit >= base:
    new_digit = str(old_digit % base) + new_digit
    old_digit = old_digit // base
new_digit = str(old_digit) + new_digit
print(new_digit)
