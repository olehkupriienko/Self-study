text = input().split()
counter = 0
for i in range(len(text)):
    if text[i].lower() == 'a' or text[i].lower() == 'an' or text[i].lower() == 'the':
        counter += 1
print('Общее количество артиклей:', counter)
