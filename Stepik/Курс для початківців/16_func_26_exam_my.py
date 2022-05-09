# объявление функции
def draw_triangle():
    for i in range(0, 8):
        print(' ' * (7 - i), '*' * (i * 2 + 1), sep='')

# основная программа
draw_triangle()  # вызов функции