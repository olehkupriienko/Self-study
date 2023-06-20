from fractions import Fraction as F
x = int(input())

result = set()

for i in range(x):
    n = i
    d = x - n
    num = F(n, d)
    if n < d and num.numerator + num.denominator == x:
        result.add(F(n, d))

print(max(result))
