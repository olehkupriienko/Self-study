import random
n = int(input())

result = [random.randint(1, 6) for _ in range(n)]
print(*result, sep='\n')