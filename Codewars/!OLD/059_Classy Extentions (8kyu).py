
class Animal:
    pass


class Cat(Animal):
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f'{self.name} meows.'


cat = Cat('Leeloo')

print(cat.speak())
