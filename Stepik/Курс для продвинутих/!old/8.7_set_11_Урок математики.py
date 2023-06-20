stud1 = set(int(i) for i in input().split())
stud2 = set(int(i) for i in input().split())
stud3 = set(int(i) for i in input().split())

s1_s2_s3 = stud1 & stud2 & stud3

result = (stud1.union(stud2).union(stud3)).difference(s1_s2_s3)

print(*sorted(result))
