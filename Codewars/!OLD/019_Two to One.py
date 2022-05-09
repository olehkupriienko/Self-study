a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"


def longest(a1, a2):
    #return (''.join(i) for i in (a1 + a2) if i not in x)

    result = ''
    temporary = sorted(a1 + a2)
    for i in temporary:
        if i not in result:
            result += i
    return result



print(longest(a, b))
