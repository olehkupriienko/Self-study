from fractions import Fraction as F

n = int(input())
fractional_numbers_list = set()

for i in range(1, n+1):
    for j in range(1, n+1):
        if F(i, j) < 1:
            fractional_numbers_list.add(F(i, j))

print(*sorted(fractional_numbers_list), sep='\n')