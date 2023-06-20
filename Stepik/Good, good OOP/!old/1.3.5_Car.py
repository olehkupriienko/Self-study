class Car:
    pass

# setattr(Car, 'model', 'Тойота')
# setattr(Car, 'color', 'Розовый')
# setattr(Car, 'number', 'П111УУ77')


new_attr = {
    'model': "Тойота",
    'color': "Розовый",
    'number': "О111АА77"
}
[setattr(Car, key, value) for key, value in new_attr.items()]


print(Car.__dict__['color'])
