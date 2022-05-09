n = int(input())

total = 0

for _ in range(1, n+1):
    if (_**2 % 10 == 2) or (_**2 % 10 == 5) or (_**2 % 10 == 8):
        total += _
print(total)
