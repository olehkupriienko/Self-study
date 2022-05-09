dig = int(input())

while dig != 0:
    last_dig = dig % 10
    print(last_dig, end='')
    dig = dig // 10
