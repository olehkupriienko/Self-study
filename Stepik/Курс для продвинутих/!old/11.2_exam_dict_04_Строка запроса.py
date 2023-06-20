test = {'sport': 'hockey', 'game': 2, 'time': 17}


def build_query_string(params: dict):
    query_string = '&'.join(f'{key}={params.get(key)}' for key in sorted(params.keys()))
    return query_string


print(build_query_string(test))
