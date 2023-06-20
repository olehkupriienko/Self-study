m = int(input())
n = int(input())


students_list = [input() for _ in range(m+n)]
students_set = set(students_list) # numbers of students


numbers_of_student = len(students_set)
numbers_of_student_who_study_two_subjects = 0
for i in students_set:
    if students_list.count(i) > 1:
        numbers_of_student_who_study_two_subjects += 1



if numbers_of_student - numbers_of_student_who_study_two_subjects:
    print(numbers_of_student - numbers_of_student_who_study_two_subjects)
else:
    print('NO')
