class DataBase:
    pk = 1
    title = 'Классы и объекты'
    author = 'Сергей Балакирев'
    views = 14356
    comments = 12


if __name__ == '__main__':
    assert DataBase.pk == 1
    assert DataBase.title == "Классы и объекты"
    assert DataBase.author == "Сергей Балакирев"
    assert DataBase.views == 14356
    assert DataBase.comments == 12
    print('All Done! Time to check!')
