with open('17.3_files_08_Обратный порядок.txt', 'r', encoding='utf-8') as file:
    text = [line.strip() for line in file][::-1]


print(*text, sep='\n')
