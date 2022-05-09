numbers = input().split()
total = 0
for i in range(len(numbers)):
    total += int(numbers[i])
print(*[i for i in numbers], sep='+', end='=')
print(total)
