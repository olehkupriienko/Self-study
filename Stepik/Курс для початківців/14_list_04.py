n = int(input())
ll = []
result = []
for _ in range(n):
    ll.append(input())
    if ll[_] not in result:
        result.append(ll[_])
print(*result, sep='\n')
