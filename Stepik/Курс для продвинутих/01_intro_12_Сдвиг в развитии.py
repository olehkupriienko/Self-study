numbers = [int(i) for i in input().split()]
numbers = [numbers[-1]] + numbers[:-1]
print(*numbers)
