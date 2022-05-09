n = int(input())
s = input()
for i in s:
    if 97 <= ord(i)-n <= 122:
        print(chr(ord(i)-n), end='')
    else:
        print(chr(ord(i)-n+122-96), end='')
