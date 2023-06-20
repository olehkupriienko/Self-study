from random import shuffle
n = int(input())

students = [input() for i in range(n)]

flag = False
while not flag:
    secret_friends = students[:]
    shuffle(secret_friends)
    for i in range(len(students)):
        if students[i] == secret_friends[i]:
            break
    else:
        flag = True

for i in range(n):
    print(f'{students[i]} - {secret_friends[i]}')
