num1 = set(int(i) for i in input().split())
num2 = set(int(i) for i in input().split())

num1 = num1.difference(num2)
print(*sorted(num1))
