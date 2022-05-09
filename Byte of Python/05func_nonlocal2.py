def func_outer():
    x = 2
    print('x равно', x)

    def func_inner():
        global x
        x = 5

    func_inner()
    print('Локальное x сменилося на', x)


func_outer()
