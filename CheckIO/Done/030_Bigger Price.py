test_limit = 2
test_data = [
        {"name": "bread", "price": 100},
        {"name": "wine", "price": 138},
        {"name": "meat", "price": 15},
        {"name": "water", "price": 1}
    ]


def bigger_price(limit: int, data: list) -> list:
    price_list = sorted([int(product.get('price')) for product in data], reverse=True)
    top_price = price_list[:limit]

    top_high_product = []

    while True:
        for item in data:
            if item.get('price') == top_price[0]:
                top_high_product.append(item)
                del top_price[0]
                break
        if len(top_price) == 0:
            break

    return top_high_product


print(bigger_price(test_limit, test_data))
