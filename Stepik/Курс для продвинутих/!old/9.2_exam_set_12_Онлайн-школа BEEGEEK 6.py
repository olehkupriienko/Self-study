m = int(input())  # кількість уроків

all_lessons = {input() for i in range(int(input()))}


for i in range(1, m):
    all_lessons = all_lessons.intersection({input() for j in range(int(input()))})

print(*sorted(all_lessons), sep='\n')