raw_ip = input()


def check_ip(line:str):
    raw_line = line.split('.')
    res = []
    for item in raw_line:
        res.append(item.isdigit() and 0 <= int(item) <= 255)
    return all(res)


print(check_ip(raw_ip))
