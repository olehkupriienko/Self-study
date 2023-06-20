test = ['a', 'a', 'bi', 'bi', 'bi']


def most_frequent(data: list) -> str:
    """
    determines the most frequently occurring string in the sequence.
    """
    # your code here
    res = max(data, key=lambda x: data.count(x))
    return res


print(most_frequent(test))
