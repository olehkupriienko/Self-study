test = [4, 6, 2, 2, 6, 4, 4, 4]
# test = [4, 4, 4, 4, 6, 6, 2, 2, 2]
# test = [1]
# test = ['bob', 'bob', 'carl', 'alex', 'bob']
# test = [17, 99, 42]



def frequency_sort(items):
    new_list = []
    for item in items:
        if [item, items.count(item)] not in new_list:
            new_list.append([item, items.count(item)])
    new_list.sort(key=lambda x: x[1], reverse=True)
    new_new_list = []
    for item in new_list:
        new_new_list.extend([item[0]] * item[1])
    return new_new_list

def frequency_sort2(items):
    return sorted(items, key=lambda x: (-items.count(x), items.index(x)))

print(frequency_sort2(test))
