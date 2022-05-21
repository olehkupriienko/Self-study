# test_list = input().split()
# m = int(input())

test_list = 'a b c d e f'.split()
m = 2


def chunked(arr, n):
    result = []
    temp_list = []
    for i in arr:
        if len(temp_list) != n:
            temp_list.append(i)
        else:
            result.append(temp_list)
            temp_list = [i]
    else:
        if test_list:
            result.append(temp_list)
    return result


print(chunked(test_list, m))
