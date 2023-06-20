class Translator:

    def __init__(self):
        self.words = {}

    def add(self, eng, rus):
        # self.words = {}
        self.words.setdefault(eng, []).append(rus)

    def remove(self, eng):
        self.words.pop(eng, False)

    def translate(self, eng):
        return self.words[eng]


tr = Translator()

tr.add('tree', 'дерево')
tr.add('car', 'машина')
tr.add('car', 'автомобиль')
tr.add('leaf', 'лист')
tr.add('river', 'река')
tr.add('go', 'идти')
tr.add('go', 'ехать')
tr.add('go', 'ходить')
tr.add('milk', 'молоко')

tr.remove('car')

print(*tr.translate('go'))
