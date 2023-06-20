# объявление функции
def get_shipping_cost(quantity):
    price = 1000 + 120 * (quantity - 1)
    return price

# считываем данные
n = int(input())

# вызываем функцию
print(get_shipping_cost(n))
