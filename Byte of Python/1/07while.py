number = 23
running = True

while running:
    guess = int(input('Введите целое число:'))
    
    if guess == number:
        print ('Поздравляю, ты угадал.')
        running = False #это останавливает цикл while
    elif guess < number:
        print ('Загаданное число больше.')
    else:
        print ('Загаданное число меньше')
else:
    print ('Цикл while закончен')

print ('Завершено')