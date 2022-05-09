s = input()
count_plus = 0
count_prod = 0

# Альтернативний варіант з вбудованою функцією .count
# count_plus = s.count('+')
# count_prod = s.count('*')
# print('Символ + встречается', count_plus, 'раз')
# print('Символ * встречается', count_prod, 'раз')

for i in range(len(s)):
    if s[i] == '*':
        count_prod += 1
    if s[i] == '+':
        count_plus += 1
print('Символ + встречается', count_plus, 'раз')
print('Символ * встречается', count_prod, 'раз')
