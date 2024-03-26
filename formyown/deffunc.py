def loop():
    for i in range(3):
        print(i)

loop()

def text_loop():
    for i in range(3):
        print('Goa is the best')

text_loop()

def new_type():
    Text = True
    Text2 = False
    print(type(Text))
    print(type(Text2))

new_type()

from typing import Union
def some_calculation(x: Union[int, float], y: Union[int, float]) -> int:
    return(x + y) ** 2

def some_calculation(x: int | float, y: int | float) -> int:
    return(x + y) ** 2

def new_variable():
    __name__ = 'berdia'
    __last__ = 'bekauri'
    __age__ = 11

def question_input():
    question = int(input('who is the best player in football history:'))
    print(question)
    print('incorrect')
    question2 = int(input('who is the best player in football history:'))
    print(question2)
    print('correct')

def variable_loop():
    x = [i for i in range(3)]
    print(x)

    y = [j for j in range(3)]
    print(y)

variable_loop()