test1 = [1, 2, 3, 1, 3]


def checkio(data: list) -> list:
    new_data = []
    for i in range(len(data)):
        if data.count(data[i]) != 1:
            new_data.append(data[i])
    data = new_data
    return data


print(checkio(test1))
