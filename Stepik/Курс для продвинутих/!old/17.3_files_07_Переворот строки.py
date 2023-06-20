with open('17.3_files_07_Переворот строки.txt', 'r', encoding='utf-8') as file:
    text = file.read()

print(text[::-1])
