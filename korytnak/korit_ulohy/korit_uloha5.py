from tkinter import *
from random import *

okno = Tk()
WIDTH, HEIGHT = 900, 600
canvas = Canvas(okno, width=WIDTH, height=HEIGHT, bg="black")
canvas.pack()

#dva nahodne obdlzniky
rect1 = [randint(0, WIDTH), randint(0, HEIGHT), randint(0, WIDTH), randint(0, HEIGHT)]
rect2 = [randint(0, WIDTH), randint(0, HEIGHT), randint(0, WIDTH), randint(0, HEIGHT)]


rect1 = [min(rect1[0], rect1[2]), min(rect1[1], rect1[3]), max(rect1[0], rect1[2]), max(rect1[1], rect1[3])]
rect2 = [min(rect2[0], rect2[2]), min(rect2[1], rect2[3]), max(rect2[0], rect2[2]), max(rect2[1], rect2[3])]

#zisti prienik
x1 = max(rect1[0], rect2[0])
y1 = max(rect1[1], rect2[1])
x2 = min(rect1[2], rect2[2])
y2 = min(rect1[3], rect2[3])

#prienik
if x1 < x2 and y1 < y2: 
    canvas.create_rectangle(rect1, fill="orange", outline="white")
    canvas.create_rectangle(rect2, fill="orange", outline="white")
    canvas.create_rectangle(x1, y1, x2, y2, fill="red", outline="white")  #prienik vyfarbeny cervenou farbou
#nie je prienik    
else:  #
    canvas.create_rectangle(rect1, fill="green", outline="white")
    canvas.create_rectangle(rect2, fill="green", outline="white")

okno.mainloop()
