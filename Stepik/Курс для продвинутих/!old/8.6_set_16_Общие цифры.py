n = int(input())

list_of_sets = [set(int(i) for i in input()) for j in range(n)]

result = list_of_sets[0]
for item in list_of_sets:
    result &= item

print(*sorted(result))
