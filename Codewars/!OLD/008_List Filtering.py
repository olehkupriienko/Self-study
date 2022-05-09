l = [1, 2, 'aasf', '1', '123', 123]
print([i for i in l if isinstance(i, int)])

def filter_list(l):
    return [i for i in l if isinstance(i, int)]
