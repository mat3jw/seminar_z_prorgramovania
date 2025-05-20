from tkinter import *
from random import *



okno = Tk()
WIDTH, HEIGHT = 900, 600
canvas = Canvas(okno, width=WIDTH, height=HEIGHT, bg="black")
canvas.pack()
stars = []


#MOON
canvas.create_oval(50, 100, 150, 200, fill="white", outline="white")
canvas.create_oval(70, 100, 170, 200, fill="black", outline="black")


#NIGHT SKY
for i in range(randint(100,1000)):
    x= randint(0, WIDTH)
    y= randint(0, HEIGHT)
    r = randint(1,4)

    color = choice(["white", "lightblue", "yellow", "orange", "red"])
    canvas.create_oval(x-r, y-r, x+r, y+r, fill= color)

#constellation
    if i < 5:
        stars.append((x, y))
if len(stars) >= 5:
    canvas.create_line(stars[0],stars[1], fill="white")
    canvas.create_line(stars[1],stars[2], fill="white")
    canvas.create_line(stars[1],stars[3], fill="white")
    canvas.create_line(stars[2],stars[4], fill="white")




okno.mainloop()