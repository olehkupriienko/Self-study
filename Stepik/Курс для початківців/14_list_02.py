n = int(input())
numbers = []

for _ in range(n):
    numbers.append(int(input()))

print(*numbers, sep='\n')
print()

for j in range(n):
    print(numbers[j]**2 + 2 * numbers[j] + 1)
