from turtle import *

start = 120
uhol = 70
pomer = 0.6
hlbka = 9

t = Turtle()
t.speed(0)
t.pencolor("white")
screen = Screen()
screen.bgcolor("black")

t.left(90)
def strom(dlzka, hlbka):
    if hlbka == 0:
        return
    t.forward(dlzka)
    t.right(uhol)
    strom(dlzka * pomer, hlbka - 1)
    t.left(2 * uhol)
    strom(dlzka * pomer, hlbka - 1)
    t.right(uhol)
    t.backward(dlzka)

strom(start, hlbka)
done()