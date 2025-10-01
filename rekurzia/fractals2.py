from turtle import *

t = Turtle()
t.speed(0)
t.pensize(2)

def vlocka(a, u):
    if a < 10:
        return
    for i in range(6):
        t.forward(a)
        vlocka(a/3, u)
        t.backward(a)
        t.right(u)

vlocka(200, 60)
mainloop()