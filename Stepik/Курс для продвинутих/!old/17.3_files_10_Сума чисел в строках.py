with open('17.3_files_10_Сума чисел в строках.txt', 'r', encoding='utf-8') as file:
    for line in file:
        print(sum(int(number) for number in line.split() if number.isdigit()))
