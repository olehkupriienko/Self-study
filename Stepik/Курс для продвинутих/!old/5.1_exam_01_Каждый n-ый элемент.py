line = input().split()
n = int(input())

result = []
count = 0
while count < n:
    result.append([line[i] for i in range(0 + count, len(line), n)])
    count += 1
print(result)
