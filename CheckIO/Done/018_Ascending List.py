# test1 = [-5, 10, -99, 123456]
test1 = []


def is_ascending(items) -> bool:
    flag = True
    for i in range(len(items)-1):
        if items[i+1] - items[i] <= 0:
            flag = False
            break
    return flag
    # return all(items[i] < items[i+1] for i in range(len(items)-1))


print(is_ascending(test1))