test = [1,2,3,4,3,2,1]


def find_even_index(arr):
    for i in range(len(arr)):
        a = sum(arr[:i])
        b = sum(arr[i+1:])
        if a == b:
            return i
    else:
        return -1



print(find_even_index(test))
