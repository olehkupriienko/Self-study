import random

file = open('17.2_files_13_Случайная строка.txt', 'r', encoding='utf-8')
text_from_file = file.readlines()
file.close()
# print(text_from_file)
random_line = text_from_file[random.randint(0, len(text_from_file)-1)]
print(random_line)
