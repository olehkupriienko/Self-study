class Human:
    pass


class Man(Human):
    def __init__(self, name):
        self.name = name
    # pass


class Woman(Human):
    def __init__(self, name):
        self.name = name


adam = Man('Adam')
eve = Woman('Eve')


def god():
    return [adam, eve]
