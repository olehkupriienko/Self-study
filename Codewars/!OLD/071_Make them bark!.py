class Dog(object):
    def __init__(self, name, breed, sex, age):
        self.name = name
        self.breed = breed
        self.sex = sex
        self.age = age


zeus = Dog('Zeus', 'Dobermann', 'male', '4')
zeus.bark = lambda: 'Woof!'
print(zeus.bark())
