# объявление функции
def get_circle(radius):
    from math import pi
    return 2 * pi * radius, pi * radius ** 2

# считываем данные
r = float(input())

# вызываем функцию
length, square = get_circle(r)
print(length, square)