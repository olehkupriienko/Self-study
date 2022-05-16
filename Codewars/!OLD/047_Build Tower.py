test = 3

def tower_builder(n):
    result = []
    for i in range (1, n+1):
        temp = ' ' * int(((n * 2 + 1) - (i * 2 + 1))/2) + '*' * (i * 2 - 1) + ' ' * int(((n * 2 + 1) - (i * 2 + 1))/2)
        result.append(temp)
    return result


print(tower_builder(test))