n = int(input())
largest1 = 0
largest2 = 0

for i in range(1, n+1):
    num = int(input())
    if num > largest2:
        largest2 = num
        if largest2 > largest1:
            largest1, largest2 = largest2, largest1

print(largest1)
print(largest2)