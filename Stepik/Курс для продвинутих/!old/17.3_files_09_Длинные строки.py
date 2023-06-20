with open('17.3_files_09_Длинные строки.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    filteret_lines = [line.strip() for line in lines if len(line) == max(len(line) for line in lines)]

print(*filteret_lines, sep='\n')