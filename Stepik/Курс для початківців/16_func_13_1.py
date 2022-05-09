def quick_merge(n):
    result = []
    for i in range(1, n+1):
        list = [int(c) for c in input().split()]
        result += list
    return sorted(result)
n = int(input())
print(*quick_merge(n))
