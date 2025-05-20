from tkinter import *


okno = Tk()
WIDTH, HEIGHT = 800, 600
canvas = Canvas(okno, width=WIDTH, height=HEIGHT)
canvas.pack()


#NEMECKO
canvas.create_rectangle(50,50,350,260, fill="black")
canvas.create_rectangle(50,120,350,260, fill="red")
canvas.create_rectangle(50,190,350,260, fill="yellow")

#TALIANSKO
canvas.create_rectangle(400,50,700,260, fill="green")
canvas.create_rectangle(500,50,700,260, fill="white")
canvas.create_rectangle(600,50,700,260, fill="red")

#FRANCUZSKO KYLIAN MBAPPE
canvas.create_rectangle(50,300,350,510, fill="blue")
canvas.create_rectangle(150,300,350,510, fill="white")
canvas.create_rectangle(250,300,350,510, fill="red")

#UKRAJINA
canvas.create_rectangle(400,300,700,510, fill="blue")
canvas.create_rectangle(400,405,700,510, fill="yellow")




okno.mainloop()