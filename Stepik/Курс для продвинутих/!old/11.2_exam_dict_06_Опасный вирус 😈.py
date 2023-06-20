numbers_of_files = int(input())
files_properties = {}

access = {'execute': 'X', 'read': 'R', 'write': 'W'}

for i in range(numbers_of_files):
    line = input()
    key, *values = line.split()
    files_properties.update({key: values})

# print(files_properties)

result = []
numbers_of_checked_files = int(input())

checked_files = {}
for i in range(numbers_of_checked_files):
    action, file = input().split()
    if access[action] in files_properties[file]:
        result.append('OK')
    else:
        result.append('Access denied')

print(*result, sep='\n')