from tkinter import *


WIDTH, HEIGHT = 800, 600
okno = Tk()
canvas = Canvas(okno, width=WIDTH, height=HEIGHT)
canvas.pack()


#canvas.create_rectangle(50, 50, 450, 250, width=3, fill="grey", outline="black")
#canvas.create_line(20, 30, 100, 200, 200, 250, fill="red", width=3, smooth=True)

def zobraz_text(position):
    canvas.create_text(position.x, position.y, text="Hello World",fill="blue", anchor="nw", font=("Arial", 20))
    print(position)

canvas.bind("<Double-Button-1>", zobraz_text)
okno.mainloop()