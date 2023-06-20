import random
n = int(input())

for i in range(n):
    x = random.randint(1, 2)
    if x == 1:
        print('Орел')
    elif x == 2:
        print('Решка')