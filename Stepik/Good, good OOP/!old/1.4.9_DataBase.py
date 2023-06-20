import sys

# программу не менять, только добавить два метода
lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока


class DataBase:
    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')

    # здесь добавлять методы
    def insert(self, data):
        for item in data:
            new_data = {}
            for key, value in zip(DataBase.FIELDS, item.split()):
                new_data[key] = value
            self.lst_data.append(new_data)

    def select(self, a, b):
        if b > len(self.lst_data):
            b = len(self.lst_data)
        return self.lst_data[a:b+1]


db = DataBase()
db.insert(lst_in)
