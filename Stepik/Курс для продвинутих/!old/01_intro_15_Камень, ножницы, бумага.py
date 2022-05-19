timur = input()
ruslan = input()


def randomizer(tim, rus):
    if tim == rus:
        return 'ничья'
    elif (tim == 'rock' and rus == 'scissors') or (tim == 'scissors' and rus == 'paper') or (
            tim == 'paper' and rus == 'rock'):
        return 'Тимур'
    else:
        return 'Руслан'


print(randomizer(timur, ruslan))
