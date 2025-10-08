def mod(func):
    def wrapper(*args, **kwargs):
        print('start')
        perem = func(*args, **kwargs)
        print('end')
        return perem
    return wrapper


@mod
def add10(x):
    return x+5
add10(100)



