with open('17.2_files_14_Сумма двух-1.txt', 'r', encoding='utf-8') as file:
    numbers = file.readlines()
    total = sum(int(number) for number in numbers)

print(total)