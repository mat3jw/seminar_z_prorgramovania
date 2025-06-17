from tkinter import *

def draw_cross(event):
    x, y = event.x, event.y
    size = 20 
    canvas.create_line(x - size, y, x + size, y, fill="black", width=2)  
    canvas.create_line(x, y - size, x, y + size, fill="black", width=2)  


okno = Tk()

canvas = Canvas(okno, width=500, height=500, bg="white")
canvas.pack()

canvas.bind("<Button-1>", draw_cross)
okno.mainloop()

