test = ['size', 12, 'in', 45, 0]


def sum_by_types(items: list) -> tuple[str, int]:
    # your code here
    str_line = ''
    dig_total = 0
    for member in items:
        if isinstance(member, str):
            str_line += member
        elif isinstance(member, int):
            dig_total += member
    return str_line, dig_total


print(sum_by_types(test))
