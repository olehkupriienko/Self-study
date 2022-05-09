s = input()
letter = ''
num_largest = 0
for i in range(len(s)):
    if s.count(s[i]) >= num_largest:
        letter = s[i]
        num_largest = s.count(s[i])
print(letter)
