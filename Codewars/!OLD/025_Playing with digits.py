test = 46288


def dig_pow2(number, p):
    total_sum = 0
    cycle = 0
    for i in str(number):
        total_sum = total_sum + int(i) ** (p + cycle)
        cycle += 1
    result = total_sum / number
    return int(result) if result.is_integer() else -1


def dig_pow(n, p):
    s = 0
    for i, c in enumerate(str(n)):
        s += pow(int(c), p+i)
    return s/n if s % n == 0 else -1


print(dig_pow(test, 3))
