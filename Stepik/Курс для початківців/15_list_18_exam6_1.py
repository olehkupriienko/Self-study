words = input().split()
words2 = []
for i in words:
    i = i[1:] + i[0] +'ки'
    words2.append(i)
print(words2)
