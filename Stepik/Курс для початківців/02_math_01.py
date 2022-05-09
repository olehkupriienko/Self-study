print('Введите три числа')
a, b, c = float(input()), float(input()), float(input())
from math import *

D = pow(b, 2) - 4 * a * c

if D>0:
    x1 = (-b+sqrt(D))/(2 * a)
    x2 = (-b-sqrt(D))/(2 * a)
    print(max(x1, x2))
    print(min(x1, x2))
elif D == 0:
    x = (-b/(2 * a))
    print(x)
else:
    print('Нет корней')