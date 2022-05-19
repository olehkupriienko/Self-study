n = 5750
d = 0


def nb_dig(n, d):

    return sum(str(i**2).count(str(d)) for i in range(0, n+1))


print(nb_dig(n, d))
