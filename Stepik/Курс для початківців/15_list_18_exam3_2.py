numbers = [int(i) for i in input().split()]
print(*[i for i in numbers], sep='+', end='=')
print(sum(numbers))
