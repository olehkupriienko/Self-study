with open('18.1_files_exam_02_Суммарная стоимость.txt', 'r', encoding='utf-8') as input_file:
    price = [int(p.lstrip('$')) for p in input_file.readlines()]

print(f'${sum(price)}')