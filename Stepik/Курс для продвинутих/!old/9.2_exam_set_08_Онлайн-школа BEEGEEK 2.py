m = int(input())  # math
n = int(input())  # computer science

math_students = {input() for _ in range(m)}
cs_students = {input() for _ in range(n)}

only_math = math_students - (math_students & cs_students)

print(len(only_math))
