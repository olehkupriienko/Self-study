import string

with open('17.3_files_12_Статистика по файлу.txt', 'r', encoding='utf-8') as file:
    text = file.readlines()
# print(text)
latin_letters = 0
words = 0
lines = len(text)

letter_of_string = string.ascii_letters
for line in text:
    words += len(line.split())
    latin_letters += sum(1 for i in line if i in letter_of_string)

print(f'Input file contains:\n{latin_letters} letters\n{words} words\n{lines} lines')


