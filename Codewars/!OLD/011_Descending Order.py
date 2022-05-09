numbers = 123456789


def descending_order(num):
    return int(''.join([j for j in sorted(str(num), reverse=True)]))


print(descending_order(numbers))
