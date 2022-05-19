numbers = [int(i) for i in input().split()]

for i in range(1, len(numbers), 2):
    numbers[i], numbers[i-1] = numbers[i-1], numbers[i]

print(*numbers)