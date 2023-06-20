test = (6, 2, '+')


def calculator(x, y, op):
    if not isinstance(x, int) or not isinstance(y, int) or str(op) not in '+-*/':
        return "unknown value"
    elif op == '+':
        return x + y
    elif op == '-':
        return x - y
    elif op == '*':
        return x * y
    elif op == '/':
        return x / y


print(calculator(*test))
