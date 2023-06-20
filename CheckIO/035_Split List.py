def split_list(items: list) -> list:
    center = int((len(items) + 1) // 2)
    return [items[:center], items[center:]]



print(split_list([1, 2, 3, 4, 5, 6]))
print(split_list([1, 2, 3]))
print(split_list([1]))
print(split_list([]))
