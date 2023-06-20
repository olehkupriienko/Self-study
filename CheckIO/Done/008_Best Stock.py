# test1 = {"CAC": 91.1, "ATX": 1.01, "TASI": 120.9}
test1 = {"CAC": 10.0, "ATX": 390.2, "WIG": 1.2}


def best_stock(data: dict) -> str:
    # largest = 0
    # for key in data.keys():
    #     if data.get(key) > largest:
    #         largest = data.get(key)
    #         stock = key
    # return stock

    return max(data, key=data.get)


print(best_stock(test1))
