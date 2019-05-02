# Имя файла func_nonlocal.py

def func_outer():
    x = 2
    print('func_outer: x равно', x)
    
    def func_inner():
        nonlocal x
        x = 5
        print('func_inner: x равно', x)

    func_inner()
    print('func_inner: Локальное x сменилось на', x)

func_outer()
   