from math import factorial

n = 5
for i in range(n):
    temp_list = []
    for j in range(i+1):
        num = (factorial(i) / (factorial(j) * factorial(i - j)))
        temp_list.append(int(num))
    print(*temp_list)
