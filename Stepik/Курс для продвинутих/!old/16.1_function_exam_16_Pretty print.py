from functools import reduce

def pretty_print(lst: list, side='-', delimiter='|'):
    length = len(lst) + reduce(lambda a, b: a + len(str(b)) + 2, lst, 0) - 1
    line = ' ' + side*length + ' '
    text = reduce(lambda a, b: f'{a} {b} {delimiter}', lst, f'{delimiter}')
    print(f'{line}\n{text}\n{line}')


pretty_print([1, 2, 10, 23, 123, 3000])
pretty_print(['abc', 'def', 'ghi', '12345'])
pretty_print(['abc', 'def', 'ghi'], side='*')
pretty_print(['abc', 'def', 'ghi'], delimiter='#')
pretty_print(['abc', 'def', 'ghi'], side='*', delimiter='#')
