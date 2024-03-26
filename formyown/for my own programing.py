#my own programing
def new_loop():
    for i in range(0,28):
        print(i)

new_loop()

def normal_loop():
    for i in range(3):
        print(i)

normal_loop()

def text_loop():
    for i in range(3):
        print('Goa is the best')

text_loop()

def new_type():
    new_type_text = True
    new_type_text2 = False
    print(new_type_text)
    print(new_type_text2)

    Text = bool('True')
    Text2 = bool('False')
    print(Text)
    print(Text2)

new_type()

def new_func():
    r = lambda q: (q * 2) - (q // 2)
    s = lambda q: (q * 3) - (q // 3)
    x = 3
    x = r(x) + s(x)
    x = r(x) - s(x)
    print(x)

new_func()

def pro_functions():
    from typing import Union

def some_calculation(x: int | float, y: int | float) -> int:
    return (x + y) ** 2

def new_variable():
    #this is me
    __name__ = 'berdia'
    __last_name__ = 'bekauri'
    __age__ = 11

def variable_loop():
    x = [i for i in range(3)]
    print(x)

    y = [j for j in range(3)]
    print(y)

variable_loop()