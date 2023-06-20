with open('17.2_files_16_Общая стоимость.txt', 'r', encoding='utf-8') as file:
    price_list = [i.strip().split('\t') for i in file.readlines()]
    # print(price_list)

print(sum([int(i[1]) * int(i[2]) for i in price_list]))
