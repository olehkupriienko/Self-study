digits_from_task1 = set(int(i) for i in input().split())
digits_from_task2 = set(int(i) for i in input().split())

same_digits = digits_from_task1 & digits_from_task2

if same_digits:
    print(*sorted(same_digits, reverse=True))
else:
    print('BAD DAY')
