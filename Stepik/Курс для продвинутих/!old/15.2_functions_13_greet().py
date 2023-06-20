
def greet2(name, *args):
    greeting = f'Hello, {name}'
    if args:
        greeting += ' and ' + ' and '.join(args)
    return greeting+'!'

def greet(name, *args):
    return f'Hello, {name}' + ' and ' + ' and '.join(args) + '!'



print(greet('Timur'))
print(greet('Timur', 'Roman'))
print(greet('Timur', 'Roman', 'Ruslan'))