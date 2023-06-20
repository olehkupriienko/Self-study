maybe_killer = {
                   'James': ['Jacob', 'Bill', 'Lucas'],
                   'Johnny': ['David', 'Kyle', 'Lucas'],
                   'Peter': ['Lucy', 'Kyle']
}
killed = ['Lucas', 'Bill']


def killer(suspect_info, dead):
    result = []
    x = len(dead)
    for key in suspect_info:
        counter = 0
        for _ in suspect_info.fromkeys(key):
            if _ in dead:
                counter += 1
            if counter == x:
                result.append(key)
    return result


print(killer(maybe_killer, killed))
