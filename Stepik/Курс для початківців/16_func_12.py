def merge(list1, list2):
#    return sorted(list1 + list2)
    list3 = list1 + list2
    list3.sort()
    return list3

print(merge([1, 2, 3], [5, 6, 7, 8]))
print(merge([1, 7, 10, 16], [5, 6, 13, 20]))
