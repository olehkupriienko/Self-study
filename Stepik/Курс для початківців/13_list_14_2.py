n = int(input())
symbols = []
for _ in range(n):
    symbols.append(input())

index = int(input())
result = ''

for s in symbols:
    if len(s) > index - 1:
        result = result + s[index - 1]
