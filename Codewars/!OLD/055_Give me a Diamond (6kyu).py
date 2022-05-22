m = 7


def diamond(num):
    if num <= 0 or num % 2 == 0:
        return None
    else:
        result = ''
        flag = num // 2 + 1
        star = 1
        while star < flag:
            result += (' ' * (flag - star) + '*' * (star * 2 - 1) + '\n')
            star += 1
        while star != 0:
            result += (' ' * (flag - star) + '*' * (star * 2 - 1) + '\n')
            star -= 1
    return result


print(diamond(m))
