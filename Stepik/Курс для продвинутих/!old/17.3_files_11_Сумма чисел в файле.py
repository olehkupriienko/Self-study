with open('17.3_files_11_Сумма чисел в файле.txt', 'r', encoding='utf-8') as file:
    total = 0
    text = file.readlines()
    for line in text:
        numbers = ''.join(line[i] if line[i].isdigit() else ' ' for i in range(len(line)))
        n = [int(_) for _ in numbers.split()]
        total += sum(n)

print(total)


