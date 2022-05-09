x = 50

def func():
    global x
    
    print('x раво', x)
    x = 2
    print('Заменяем глобальое зачение x на', x)
    
func()
print('Значение x теперь составляет', x)