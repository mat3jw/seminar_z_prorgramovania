from turtle import *

zofka = Turtle()
zofka.speed(1)
zofka.pensize(2)
zofka.left(90)

def strom(a):

    zofka.forward(a)
    zofka.left(45)
    zofka.forward(a//2)
    
    if a > 40:
        strom(a//2)

    zofka.backward(a//2)
    zofka.right(2*30)
    zofka.forward(a//2)
    
    if a > 40:
        strom(a//2)

    zofka.backward(a//2)
    zofka.left(45)
    zofka.backward(a)
#nefunkcne



strom(100)
mainloop()