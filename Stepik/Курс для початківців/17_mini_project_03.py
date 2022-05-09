from random import *
n = randint(1, 100)
print('Добро пожаловать в числовую угадайку')
def is_valid(num):
    return num.isdigit() and 1 <= int(num) <= 100
def is_valid_num():
    while True:
        print('Введите Ваше число:')
        num = input()
        if is_valid(num):
            return int(num)
        else:
            print('А может быть все-таки введем целое число от 1 до 100?')
def compare():
    while True:
        num = is_valid_num()
        if n < num:
            print('Ваше число меньше загаданного, попробуйте еще разок')
        elif n > num:
            print('Ваше число больше загаданного, попробуйте еще разок')
        else:
            print('Вы угадали, поздравляем!')
            break
compare()