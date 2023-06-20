with open('17.2_files_15_Сумма двух-2.txt', 'r', encoding='utf-8') as file:
    text = file.read()
    numbers = (int(i) for i in text.split())
print(sum(numbers))