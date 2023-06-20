stud1 = set(int(i) for i in input().split())
stud2 = set(int(i) for i in input().split())
stud3 = set(int(i) for i in input().split())

result = sorted(set(range(0, 11)).difference(stud1 | stud2 | stud3))

print(*result)
