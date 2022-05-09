test1 = [20, 37, 20, 21]
test2 = 1


def delete_nth(order, max_e):
    # code here
    result = []
    for i in order:
        if result.count(i) < max_e:
            result.append(i)
    return result


print(delete_nth(test1, test2))
