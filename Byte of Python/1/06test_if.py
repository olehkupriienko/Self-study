number = 23
guess = int(input('Введите целое число:'))
if guess == number:
    print ('''Вы угадали
Хотя и не выиграли никакого приза''')
    
elif guess < number:
    print ('Загаданое чило больше')
else:
    print ('Нет, загаданное чило меньше')
print ('Завершено')