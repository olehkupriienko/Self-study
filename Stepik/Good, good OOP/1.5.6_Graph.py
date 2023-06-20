# здесь объявляются все необходимые классы
class Graph:

    def __init__(self, data):
        self.data = data[:]
        self.is_show = True

    def set_data(self, new_data):
        self.data = new_data[:]

    def _get_data_in_str(self):
        return ' '.join(map(str, self.data))

    def show_table(self):
        if self.is_show is True:
            print(' '.join(self._get_data_in_str()))
        else:
            print("Отображение данных закрыто")

    def show_graph(self):
        if self.is_show is True:
            print(f"Графическое отображение данных: {self._get_data_in_str()}")
        else:
            print("Отображение данных закрыто")

    def show_bar(self):
        if self.is_show is True:
            print(f"Столбчатая диаграмма: {self._get_data_in_str()}")
        else:
            print("Отображение данных закрыто")

    def set_show(self, fl_show):
        self.is_show = fl_show


# считывание списка из входного потока (эту строку не менять)
# data_graph = list(map(int, input().split()))
data_graph = list(map(int, '8 11 10 -32 0 7 18'.split()))
gr = Graph(data_graph)

# здесь создаются объекты классов и вызываются нужные методы
gr.show_bar()
gr.set_show(False)
gr.show_table()
