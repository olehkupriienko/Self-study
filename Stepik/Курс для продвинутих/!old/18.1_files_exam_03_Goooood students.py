with open('18.1_files_exam_03_Goooood students.txt', 'r', encoding='utf-8') as grades_file:
    counter = 0
    for line in grades_file:
        name, *args = line.split()
        if all(int(arg) >= 65 for arg in args):
            counter += 1

print(counter)
