test = '45385593107843568'


def fake_bin(x):
    return ''.join('0' if int(i) < 5 else '1' for i in x)


print(fake_bin(test))
