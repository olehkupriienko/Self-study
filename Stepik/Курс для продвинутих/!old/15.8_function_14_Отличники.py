number_of_classes = int(input())
res = []

for i in range(number_of_classes):
    study_class = {}
    m = int(input())
    for j in range(m):
        key, value = input().split(' ')
        study_class.setdefault(value, []).append(key)
    res.append(study_class)

if all(map(lambda x: '5' in x, res)):
    print('YES')
else:
    print('NO')
