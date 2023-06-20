test1 = []


def all_the_same(elements: list) -> bool:
    return 0 <= len(set(elements)) <= 1


print(all_the_same(test1))
