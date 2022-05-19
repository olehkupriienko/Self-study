zodiak = ['Дракон', 'Змея', 'Лошадь', 'Овца', 'Обезьяна', 'Петух', 'Собака', 'Свинья', 'Крыса', 'Бык', 'Тигр', 'Заяц']

year = int(input())

if year > 2011:
    while year > 2011:
        year -= 12
if year < 2000:
    while year < 2000:
        year += 12

print(zodiak[year - 2000])
