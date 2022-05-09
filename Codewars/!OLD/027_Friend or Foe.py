test = ["Ryan", "Kieran", "Jason", "Yous"]


def friend(x):
    return [i for i in x if len(i) == 4]



print(friend(test))
