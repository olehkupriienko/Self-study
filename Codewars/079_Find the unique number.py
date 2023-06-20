test = [0, 0, 0.55, 0, 0]


def find_uniq(arr):
    # your code here
    uniq_items = set(arr)
    for item in uniq_items:
        if arr.count(item) == 1:
            return item


print(find_uniq(test))
