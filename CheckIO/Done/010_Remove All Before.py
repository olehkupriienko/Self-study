from typing import Iterable
test1 = [1, 1, 2, 2, 3, 3]
test2 = 0


def remove_all_before(items: list, border: int) -> Iterable:
    if border in items:
        first_index = items.index(border)
        items = items[first_index:]
    return items



print(remove_all_before(test1, test2))
