lines = int(input())
numbers = []

for i in range(lines):
    numbers += [int(input())]

main_digit = int(input())
flag = 'НЕТ'
for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
        if numbers[i] * numbers[j] == main_digit:
            flag = 'ДА'
            break
    if flag == 'ДА':
        break

print(flag)
