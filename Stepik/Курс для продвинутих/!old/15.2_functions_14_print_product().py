def print_products(*args):
    counter = 0
    product_list = []
    for arg in args:
        if type(arg) == str and len(arg) > 0:
            product_list.append(arg)
    if product_list:
        for product in product_list:
            counter += 1
            print(f'{counter}) {product}')
    else:
        print('Нет продуктов')


print_products('Бананы', [1, 2], ('Stepik',), 'Яблоки', '', 'Макароны', 5, True)
print_products([4], {}, 1, 2, {'Beegeek'}, '')
