def quick_merge(n):
    return sorted([int(c) for i in range(n) for c in input().split()])
n = int(input())
print(*quick_merge(n))
