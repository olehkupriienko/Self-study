stud1 = set(int(i) for i in input().split())
stud2 = set(int(i) for i in input().split())
stud3 = set(int(i) for i in input().split())

result = sorted(stud3.difference(stud1.union(stud2)), reverse=True)

print(*result)
