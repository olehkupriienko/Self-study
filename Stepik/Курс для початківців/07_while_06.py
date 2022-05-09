dig = int(input())

while dig // 10 != 0:
    pre_last_digit = dig % 10
    dig = dig // 10

print(pre_last_digit)
