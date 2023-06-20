n = int(input())
students = tuple(tuple(int(_) if _.isdigit() else _ for _ in input().split()) for __ in range(n))

for student in students:
    print(*student)
print()
for student in students:
    if student[-1] >= 4:
        print(*student)
