s = input()
counter = 0
for i in range(len(s)):
    if '0' <= s[i] <= '9':
        counter += 1
print(counter)
