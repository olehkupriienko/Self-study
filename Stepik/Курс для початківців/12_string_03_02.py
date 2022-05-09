s = input()
cont = 0
for i in s:
    if i != i.upper():
        cont += 1
print(cont)
