# объявление функции
def is_magic(date):
    date2 = [int(i) for i in date.split('.')]
    return date2[0] * date2[1] == date2[2] % 100

# считываем данные
date = input()

# вызываем функцию
print(is_magic(date))