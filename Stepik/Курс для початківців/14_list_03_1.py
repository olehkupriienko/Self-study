n, temp = int(input()), []
for i in range(n):
    temp.append(int(input()))
for num in temp:
    if min(temp) < num < max(temp):
        print(num)