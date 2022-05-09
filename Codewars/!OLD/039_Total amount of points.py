test = ['1:1','2:2','3:3','4:4','2:2','3:3','4:4','3:3','4:4','4:4']


def points(games):
    points = 0
    for i in games:
        cycle = [int(_) for _ in i.split(':')]
        if cycle[0] > cycle[1]:
            points += 3
        elif cycle[0] == cycle[1]:
            points += 1
    return points


print(points(test))
