lines = int(input())
q_1, q_2, q_3, q_4 = 0, 0, 0, 0

for i in range(lines):
    a, b = (int(i) for i in input().split())
    if a > 0 and b > 0:
        q_1 += 1
    elif a < 0 and b > 0:
        q_2 += 1
    elif a < 0 and b < 0:
        q_3 += 1
    elif a > 0 and b < 0:
        q_4 += 1

print(f'Первая четверть: {q_1}\nВторая четверть: {q_2}\nТретья четверть: {q_3}\nЧетвертая четверть: {q_4}')
