test = 'Two words'


def wave(people):
    temp = people.lower()
    result = []
    for i in range(len(temp)):
        if temp[i] == ' ':
            continue
        else:
            result2 = temp[:i] + temp[i].upper() + temp[i+1:]
            result.append(result2)
    return result


print(wave(test))
