from turtle import *

zofka = Turtle()
zofka.speed(10.5)
zofka.pensize(3)

def strom(a):

    zofka.left(90)
    zofka.forward(a)
    zofka.left(45)
    zofka.forward(a/2)
    
    if a > 10:
        strom(a/2)

    zofka.backward(a/2)
    zofka.right(90)
    zofka.forward(a/2)
    
    if a > 10:
        strom(a/2)

    zofka.backward(a/2)
    zofka.left(45)
    zofka.backward(a)
    zofka.right(90)



strom(100)
mainloop()