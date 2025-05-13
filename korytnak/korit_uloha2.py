from tkinter import *


okno = Tk()
WIDTH, HEIGHT = 800, 600
canvas = Canvas(okno, width=WIDTH, height=HEIGHT)
canvas.pack()

#KRUHY VLAJKY
canvas.create_oval(50, 50, 250, 250, outline="blue", width=30)
canvas.create_oval(175,150,375,350, outline="yellow", width=30)
canvas.create_oval(300,50,500,250, outline="black", width=30)
canvas.create_oval(425,150,625,350, outline="green", width=30)
canvas.create_oval(550,50,750,250, outline="red", width=30)




okno.mainloop()