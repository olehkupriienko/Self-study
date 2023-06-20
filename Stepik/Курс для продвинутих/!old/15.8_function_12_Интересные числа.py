a, b = int(input()), int(input())

numbers = list(range(a, b+1))
res = []
for num in numbers:
    for i in str(num):
        if i == '0' or num % int(i) != 0:
            break
    else:
        res.append(num)

print(*res)


result = [i for i in range(a, b+1) if all(map(lambda x: ))]