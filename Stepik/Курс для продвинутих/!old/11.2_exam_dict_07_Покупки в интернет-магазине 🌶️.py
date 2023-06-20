from pprint import pprint
n = int(input())
shop_list = {}

for _ in range(n):
    name, goods, quantity = input().split()
    shop_list.setdefault(name, {}).update({goods: shop_list[name].get(goods, 0) + int(quantity)})

pprint(shop_list)

for name in sorted(shop_list.keys()):
    print(name + ':')
    for goods in sorted(shop_list[name].keys()):
        print(f'{goods} {shop_list[name][goods]}')
