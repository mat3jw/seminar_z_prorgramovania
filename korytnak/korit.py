from tkinter import *


WIDTH, HEIGHT = 800, 600
okno = Tk()
canvas = Canvas(okno, width=WIDTH, height=HEIGHT)
canvas.pack()


canvas.create_rectangle(50, 50, 450, 250, width=3, fill="grey", outline="black")
canvas.create_line(20, 30, 100, 200, 200, 250, fill="red", width=3, smooth=True)
canvas.create_text(20, 30, text="Hello World",fill="blue", anchor="nw", font=("Arial", 20))

okno.mainloop()