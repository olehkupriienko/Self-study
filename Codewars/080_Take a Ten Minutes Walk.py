test = ['s', 'n', 'e', 'n', 'n', 'n', 's', 'w', 's', 's']


# CLEVER
def isValidWalk(walk):
    if (walk.count('n') == walk.count('s') and
            walk.count('e') == walk.count('w') and
            len(walk) == 10):
        return True
    return False


def is_valid_walk(walk):
    walk.sort()
    if len(walk) != 10:
        return False
    else:
        flag = True
        while flag and walk:
            for i in range(len(walk) - 1):
                # condition  N - S
                if (walk[i] == 'n' and walk[i + 1] == 's') or (walk[i] == 's' and walk[i + 1] == 'n'):
                    del walk[i + 1]
                    del walk[i]
                    break
                elif (walk[i] == 'w' and walk[i + 1] == 'e') or (walk[i] == 'e' and walk[i + 1] == 'w'):
                    del walk[i + 1]
                    del walk[i]
                    break
            else:
                flag = False
        return flag


print(is_valid_walk(test))
