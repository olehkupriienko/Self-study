n = int(input())
symbols = []
for i in range(n):
    symbols.append(input())

k = int(input())
result = ''

for j in range(n):
    new_symbol = symbols[j]
    if len(new_symbol) > k - 1:
        result += new_symbol[k - 1]
print(result)
