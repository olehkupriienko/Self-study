import random

# numbers = random.sample(range(1, 100), 25)
numbers = '\n'.join(str(i) for i in random.sample(range(111, 778), 25))

with open('random.txt', 'w', encoding='utf-8') as f:
    f.write(numbers)
