words = input().split()

flag = 'YES'

for i in range(len(words)-1):
    if set(words[i]) != set(words[i+1]):
        flag = 'NO'
        break

print(flag)