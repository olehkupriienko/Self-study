text = input().split()
for i in range(len(text)):
    text[i] = int(text[i])
largest = max(text)
smallest = min(text)
max_index = text.index(largest)
min_index = text.index(smallest)
text[max_index] = smallest
text[min_index] = largest

print(*text)
