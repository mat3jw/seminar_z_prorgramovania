from tkinter import *


WIDTH, HEIGHT = 800, 600
okno = Tk()
canvas = Canvas(okno, width=WIDTH, height=HEIGHT)
canvas.pack()


def text(position):
    canvas.create_text(position.x, position.y, text="cafko",fill="blue", anchor="nw", font=("Arial", 20))
    canvas.create_text(WIDTH - position.x, position.y, text="cafko",fill="blue", anchor="nw", font=("Arial", 20))
    canvas.create_text(position.x, HEIGHT - position.y, text="cafko",fill="blue", anchor="nw", font=("Arial", 20))
    canvas.create_text(WIDTH - position.x, HEIGHT - position.y, text="cafko",fill="blue", anchor="nw", font=("Arial", 20))




canvas.bind("<Double-Button-1>", text)
okno.mainloop()