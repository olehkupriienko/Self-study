num = int(input())
total, digits, product, last_digit = 0, 0, 1, num % 10

while num != 0:
    total = total + num % 10
    digits +=  1
    product *= (num % 10)
    first_dig = num % 10
    num //= 10

print(total, digits, product, total/digits, first_dig, first_dig + last_digit, sep='\n')
