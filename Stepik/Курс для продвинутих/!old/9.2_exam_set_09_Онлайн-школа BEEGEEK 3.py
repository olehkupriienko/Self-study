m = int(input())  # math
n = int(input())  # computer science

math_students = {input() for _ in range(m)}
cs_students = {input() for _ in range(n)}

only_math_or_cs = math_students ^ cs_students

if only_math_or_cs:
    print(len(only_math_or_cs))
else:
    print('NO')