students1 = {i for i in input().split()}
students2 = {i for i in input().split()}

students = students1 | students2

print(*sorted(students))
