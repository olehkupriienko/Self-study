# test = [{'a': 1, 'b': 2}, {'b': 10, 'c': 100}, {'a': 1, 'b': 17, 'c': 50}, {'a': 5, 'd': 777}]
test = [{'a': 1, 'b': 2}, {'b': 10, 'c': 100}, {'a': 1, 'b': 17, 'c': 50}, {'a': 5, 'd': 777}]


def merge(values: list):      # values - это список словарей
    new_dict = {}
    for i_dict in values:
        for k, v in i_dict.items():
            new_dict.setdefault(k, set()).add(v)
    return new_dict


print(merge(test))
