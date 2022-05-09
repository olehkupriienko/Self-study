from math import factorial

n = int(input())
suma = 0

for i in range(1, n+1):
    suma = suma + factorial(i)
print(suma)
