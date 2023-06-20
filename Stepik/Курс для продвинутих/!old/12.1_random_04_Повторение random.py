import random

lottery_numbers = set()

while len(lottery_numbers) != 7:
    lottery_numbers.add(random.randint(1, 49))

# print(' '.join(str(i) for i in sorted(lottery_numbers)))
print(*sorted(lottery_numbers))
