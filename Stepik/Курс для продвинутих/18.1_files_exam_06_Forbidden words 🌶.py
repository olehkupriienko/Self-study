file_name = '18.1_files_exam_06_textfile.txt'
# file_name = input()

with open('18.1_files_exam_06_forbidden_words.txt', 'r') as f:
    forbidden_words = f.read().split()

with open(file_name, 'r') as f:
    text = f.read()

temp_text = text.lower()[:]

for word in forbidden_words:
    temp_text = temp_text.replace(word, '*' * len(word))

result_text = ''
for i in range(len(temp_text)):
    if temp_text[i] == '*':
        result_text += '*'
    else:
        result_text += text[i]

print(result_text)
