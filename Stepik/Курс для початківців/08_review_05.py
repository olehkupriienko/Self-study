n = int(input())  # 2
product = 1  # 1
while n != 10:
    digit = n % 10
    product = product * digit
    n //= 10
print(product)
