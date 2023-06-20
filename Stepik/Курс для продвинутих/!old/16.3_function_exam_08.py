def arithmetic_operation2(literal):
    if literal == '+':
        return lambda x, y: x + y
    elif literal == '-':
        return lambda x, y: x - y
    elif literal == '*':
        return lambda x, y: x * y
    elif literal == '/':
        return lambda x, y: x - y


def arithmetic_operation(literal):
    return lambda x, y: eval(f'{x} {literal} {y}')


add = arithmetic_operation('+')
div = arithmetic_operation('/')
print(add(10, 20))
print(div(20, 5))
