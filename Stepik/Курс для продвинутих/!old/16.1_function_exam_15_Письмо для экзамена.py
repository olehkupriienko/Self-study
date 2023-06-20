
def generate_letter(mail, name, date, time, place, /, teacher='Тимур Гуев', number=17):
    return f'To: {mail}\nПриветствую, {name}!\nВам назначен экзамен, который пройдет {date}, в {time}.\n\
По адресу: {place}.\nЭкзамен будет проводить {teacher} в кабинете {number}.\nЖелаем удачи на экзамене!'


def generate_letter2(mail, name, date, time, place, teacher=None, number=None):
    if not teacher:
        teacher = 'Тимур Гуев'
    if not number:
        number = 17
    return f'To: {mail}\nПриветствую, {name}!\nВам назначен экзамен, который пройдет {date}, в {time}.\n\
По адресу: {place}.\nЭкзамен будет проводить {teacher} в кабинете {number}.\nЖелаем удачи на экзамене!'


print(generate_letter('lara@yandex.ru', 'Лариса', '10 декабря', '12:00', 'Часова 23, корпус 2'))
print()
print(generate_letter('lara@yandex.ru', 'Лариса', '10 декабря', '12:00', 'Часова 23, корпус 2', 'Василь Ярошевич', 23))