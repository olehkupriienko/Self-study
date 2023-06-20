test = 'Mex'


def who_is_paying(name):
    return [name[:2], name] if len(name) > 2 else [name]


print(who_is_paying(test))
