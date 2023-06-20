test1 = '1'
test2 = '1'


def add_binary(a, b):
    digit = int(a)+int(b)
    return f'{digit:b}'


print(add_binary(test1, test2))
