n, temp = int(input()), []
for i in range(n):
    temp.append(int(input()))
del temp[temp.index(min(temp))]
del temp[temp.index(max(temp))]
print(*temp, sep='\n')