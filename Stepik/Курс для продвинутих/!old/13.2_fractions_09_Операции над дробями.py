from fractions import Fraction as F

digit1 = input()
digit2 = input()

print(f'{digit1} + {str(digit2)} = {F(digit1) + F(digit2)}')
print(f'{digit1} - {str(digit2)} = {F(digit1) - F(digit2)}')
print(f'{digit1} * {str(digit2)} = {F(digit1) * F(digit2)}')
print(f'{digit1} / {str(digit2)} = {F(digit1) / F(digit2)}')
