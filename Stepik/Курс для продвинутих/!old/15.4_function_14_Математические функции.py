import math
operations = {'квадрат': lambda x: x**2, 'куб': lambda x: x**3, 'корень': lambda x: x**0.5,
              'модуль': lambda x: abs(x), 'синус': lambda x: math.sin(x)}


def operate(x, operation):
    return operations[operation](x)


n = int(input())
oper = input()

print(operate(n, oper))
