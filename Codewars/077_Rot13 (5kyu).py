test1 = 'Test'


def rot13(message: str):
    alfabet_lower = 'abcdefghijklmnopqrstuvwxyz'
    alfabet_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = ''
    for _ in message:
        if _ in alfabet_lower:
            result += alfabet_lower[((alfabet_lower.index(_) + 13) % 26)]
        elif _ in alfabet_upper:
            result += alfabet_upper[((alfabet_upper.index(_) + 13) % 26)]
        else:
            result += _
    return result


print(rot13(test1))

