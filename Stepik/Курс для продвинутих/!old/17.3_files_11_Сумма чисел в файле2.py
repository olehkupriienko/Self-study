with open('17.3_files_11_Сумма чисел в файле2.txt', 'r', encoding='utf-8') as file:
    text = file.read()
    numbers = ''.join(text[i] if text[i].isdigit() else ' ' for i in range(len(text)))
    total = sum([int(_) for _ in numbers.split()])

print(total)


