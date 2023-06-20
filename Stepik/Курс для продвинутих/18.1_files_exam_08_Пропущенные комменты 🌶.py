file_name = '18.1_files_exam_08_Пропущенные комменты 🌶.txt'

with open(file_name, 'r') as input_file:
    text = [line.strip() for line in input_file.readlines()]

list_of_commented_functions = []
for i in range(len(text)-1):
    if i == 0:
        if text[i].startswith('def'):
            list_of_commented_functions.append(text[i].split(' ')[1])
    elif text[i].startswith('def') and not text[i-1].startswith('#'):
        list_of_commented_functions.append(text[i].split(' ')[1])

if list_of_commented_functions:
    for item in list_of_commented_functions:
        print(item.split('(')[0])
else:
    print('Best Programming Team')
