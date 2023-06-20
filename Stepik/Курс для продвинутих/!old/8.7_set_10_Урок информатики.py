student_1 = set(int(i) for i in input().split())
student_2 = set(int(i) for i in input().split())
student_3 = set(int(i) for i in input().split())

s1_s2 = student_1 & student_2

s1_s2_s3 = s1_s2 - student_3

lst3 = sorted(s1_s2_s3, reverse=True)
print(*lst3)
