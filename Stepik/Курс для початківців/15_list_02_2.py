text = input().split()
for i in range(len(text)):
    text[i] = int(text[i])
max_index = text.index(max(text))
min_index = text.index(min(text))
text[max_index], text[min_index] = text[min_index], text[max_index]

print(*text)
