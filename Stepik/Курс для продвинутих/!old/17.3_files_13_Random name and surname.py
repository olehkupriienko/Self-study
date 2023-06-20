from random import randint
with open('17.3_files_13_first_names.txt', 'r') as first_names_file, open('17.3_files_13_last_names.txt', 'r') as last_names_file:
    name = [i.strip() for i in first_names_file.readlines()]
    surname = [i.strip() for i in last_names_file.readlines()]
print(name[randint(0, len(name) - 1)] + ' ' + surname[randint(0, len(surname) - 1)])
print(name[randint(0, len(name) - 1)] + ' ' + surname[randint(0, len(surname) - 1)])
print(name[randint(0, len(name) - 1)] + ' ' + surname[randint(0, len(surname) - 1)])