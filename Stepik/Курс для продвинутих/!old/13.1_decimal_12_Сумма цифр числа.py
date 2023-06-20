# from decimal import Decimal as dec
#
# digit_as_string = input("Введите число: ")
# digits_list = [dec(digit) for digit in digit_as_string if digit.isdigit()]
# print(min(digits_list) + max(digits_list))


from decimal import *
num = Decimal(input())
# Сохраняем кортеж из цифр числа.
digits = num.as_tuple().digits

# Добавляем в кортеж ноль, если число вида: 0.123
if len(digits) == abs(num.as_tuple().exponent):
    digits = (0, ) + digits

# Выводим сумму наименьшего и наибольшего Decimal числа.
print(min(digits) + max(digits))