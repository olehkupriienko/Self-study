test = 'patrick feenan'


def abbrev_name2(name):
    return (name[0] + '.' + name[name.index(' ')+1]).upper()


def abbrev_name(name):
    return '.'.join(w[0] for w in name.split()).upper()


print(abbrev_name(test))

