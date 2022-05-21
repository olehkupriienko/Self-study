new_word = input().replace(' ', '')
finish_list = []

temp_list = [new_word[0]]
for i in range(1, len(new_word)):
    if new_word[i] in temp_list:
        temp_list.append(new_word[i])
    else:
        finish_list.append(temp_list)
        temp_list = list(new_word[i])
else:
    finish_list.append(temp_list)

print(finish_list)
