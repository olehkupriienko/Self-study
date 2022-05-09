def printMax (a, b):
    if a > b:
        print (a, 'максимум')
    elif a == b:
        print (a, 'раво', b)
    else:
        print (b, 'максимум')

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))

printMax (a, b)