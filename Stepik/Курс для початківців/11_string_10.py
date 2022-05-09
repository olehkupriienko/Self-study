num = int(input())
new_dig = ''
while num != 0:
    new_dig = str(num % 2) + new_dig
    num = num // 2
print(new_dig)
