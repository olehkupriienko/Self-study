w, h = float(input()), float(input())
IMT = w / h ** 2
if IMT < 18.5:
    print('Недостаточная масса')
elif 18.5 <= IMT <= 25:
    print('Оптимальная масса')
else:
    print('Избыточная масса')