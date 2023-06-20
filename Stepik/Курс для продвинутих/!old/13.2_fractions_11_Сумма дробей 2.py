from math import factorial
from fractions import Fraction as F

n = int(input())
total = 0
for _ in range(n):
    total += F(1, factorial(_ + 1))

print(total)
