lst_line = input().split()

my_dict = {}
for key in lst_line:
    my_dict[key] = my_dict.get(key, 0) + 1
    print(my_dict[key], end=' ')

