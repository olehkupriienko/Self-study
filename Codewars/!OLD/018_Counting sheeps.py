sheeps = [True, True, True, False,
          True, True, True, True,
          True, False, True, False,
          True, False, False, True,
          True, True, True, True,
          False, False, True, True]


def count_sheeps(sheep):
    # TODO May the force be with you
    #return sheep.count(True)
    return sum([i for i in sheep if i])



print(count_sheeps(sheeps))
