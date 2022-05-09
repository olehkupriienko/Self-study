n = int(input().lstrip('#'))

for i in range(n):
    text = input()
    if '#' in text:
        text = text[:text.index('#')]
    print(text.rstrip())
