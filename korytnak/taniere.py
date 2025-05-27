from tkinter import *


WIDTH, HEIGHT = 800, 600
okno = Tk()
canvas = Canvas(okno, width=WIDTH, height=HEIGHT, bg="black")
canvas.pack()
S = [150,150]
r = 100
t1 = [S[0] - r, S[1] - r]
t2 = [S[0] + r, S[1] + r]


canvas.create_oval(50,50,250,250, fill="blue", outline="white", width=4)
canvas.create_text(150,150, text= "A", fill="white", font=("Arial", 24, "bold"))


def zisti_kliknutie(x):

    if t1[0] <= x.x <= t2[0] and t1[1] <= x.y <= t2[1]:
        print("Klikol si na kruh!")  
    else:
        print("Klikol si mimo kruhu!")

canvas.bind("<Button-1>", zisti_kliknutie)
okno.mainloop()