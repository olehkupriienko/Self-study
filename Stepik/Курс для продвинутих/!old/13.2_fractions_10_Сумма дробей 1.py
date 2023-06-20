from fractions import Fraction as F

n = int(input())

total = F(0)
for i in range(n):
    total += F(1, (i + 1)**2)
print(total)
