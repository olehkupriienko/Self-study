list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]

# інший варіант виконання за допомогою додаткового списку
# res = []
# for items in list1:
#     res.append(items[::-1])
# list1 = res

for items in list1:
    items.reverse()

print(list1)
