n = 3
my_list = []
for i in range(1, n+1):
    temp_list = []
    for j in range(1, n+1):
        temp_list.append(j)
    print(temp_list)
print(*my_list, sep='\n')
# print()

print(*[[j for j in range(1, n+1)] for i in range(1, n+1)], sep='\n')
