s = input()
cont = 0
for i in s:
    if not i.islower():
        continue
    cont += 1
print(cont)
