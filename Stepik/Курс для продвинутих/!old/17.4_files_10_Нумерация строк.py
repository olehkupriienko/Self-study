# with open('17.4_files_10_Нумерация строк.txt', 'r') as input_file:
#     text = input_file.read()
#
# new_text = '\n'.join(f'{i + 1}) {line}' for i, line in enumerate(text.split('\n')))
#
# with open('output.txt', 'w') as output_file:
#     output_file.write(new_text)



with open('17.4_files_10_Нумерация строк.txt', 'r') as input_file, open('output.txt', 'w') as output_file:
    text = input_file.read()
    new_text = '\n'.join(f'{i + 1}) {line}' for i, line in enumerate(text.split('\n')))
    output_file.write(new_text)
