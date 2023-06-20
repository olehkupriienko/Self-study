class Goods:
    title = "Мороженое"
    weight = 154
    tp = "Еда"
    price = 1024


# Goods.price = 2048
# Goods.inflation = 100

setattr(Goods, 'price', 2048)
setattr(Goods, 'inflation', 100)


assert Goods.title == "Мороженое"
assert Goods.weight == 154
assert Goods.tp == "Еда"
assert Goods.price == 2048
assert Goods.inflation == 100, "неверные значения атрибутов"
print('All Done! Time to check!')
