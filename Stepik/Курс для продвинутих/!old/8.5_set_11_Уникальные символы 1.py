n = int(input())

res = [len(set(input().lower())) for _ in range(n)]
print(*res, sep='\n')
