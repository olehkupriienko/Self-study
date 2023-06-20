t = 555


def to_binary(n):
    return int(f'{n:b}')
    # return int(bin(n).replace('0b', ''))
    # return int(bin(n)[2:])


print(to_binary(t))
