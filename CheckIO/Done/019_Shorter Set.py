test_set = {8, 9, 7}
# test_set = {1, 2, 7, 8, 9}

# num_of_iteration = 0
# num_of_iteration = 1
num_of_iteration = 2


def remove_min_max(data: set, total: int) -> set:
    # your code here
    res = list(data)
    for i in range(total):
        if res:
            res.pop(res.index(max(res)))
        if res:
            res.pop(res.index(min(res)))
    return set(res)


print(remove_min_max(test_set, num_of_iteration))
