numbers = input().split(' ')
counter = 0

for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
        if numbers[j] == numbers[i]:
            counter += 1
print(counter)
