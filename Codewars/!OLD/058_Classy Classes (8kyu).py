name_name = 'Oleh'
age_age = 31


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.info = f'{self.name} is {self.age} years old'


person1 = Person(name_name, age_age)
print(person1.name, person1.age)
print(person1.info)
