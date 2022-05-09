test = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]


def sort_array(source_array):
    temp = sorted(i for i in source_array if i % 2 == 1)
    for i in range(len(source_array)):
        if source_array[i] % 2 == 1:
            source_array[i] = temp.pop(0)
    return source_array


print(sort_array(test))
