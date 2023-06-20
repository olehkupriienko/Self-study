class Person:
    def __init__(self, name):
        self.name = name

    def greet(self, your_name):
        return f'Hello {your_name}, my name is {self.name}'


jack = Person("Jack")
jill = Person("Jill")
joe = Person('Joe')

print(joe.greet('Kate')) # should return 'Hello Kate, my name is Joe'
print(joe.name)

