flag = 'Цифр нет'
s = input()

for i in range(len(s)):
    if s[i] in '0123456789':
        flag = 'Цифра'
        break
print(flag)