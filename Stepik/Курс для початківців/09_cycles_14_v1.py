n = int(input())
suma = 0

for i in range(1, n+1):
    product_j = 1
    for j in range(1, i+1):
        product_j = product_j * j
    suma = suma + product_j
print(suma)
