n = int(input())

result = len(set(''.join(input().lower() for _ in range(n))))
print(result)

# res = sum([len(set(''.join(i for i in input().lower()))) for _ in range(n)]
# print(*res, sep='\n')
