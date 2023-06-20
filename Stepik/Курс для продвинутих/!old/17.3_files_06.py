with open('17.3_files_06.txt', encoding='utf-8') as file:
    print('Repeat after me:', file.readline().strip())
    for line in file:
        print(line.strip() + '!')
    print('I am not here anymore.')