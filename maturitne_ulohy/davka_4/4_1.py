from tkinter import *
from random import *

letters = "ABCDEFGHIJKL"
stvorcekov = len(letters)
sirka = 50
medzera = 20

sirka_okna = stvorcekov * sirka + (stvorcekov + 1) * medzera
vyska_okna = sirka + 2 * medzera

window = Tk()
canvas = Canvas(window, width= sirka_okna, height= vyska_okna)
canvas.pack()

x, y = medzera, medzera
for i in range(stvorcekov):
    canvas.create_rectangle(x, y, x + sirka, y + sirka, fill="green")
    canvas.create_text(x + sirka / 2, y + sirka / 2, text=letters[i], font=("Arial", 20), fill = "white")
    x += sirka + medzera
    
def kruzok(suradnice):
    utvar = canvas.find_withtag("current")
    canvas.itemconfig(utvar, fill = "red")



canvas.bind("<Button-1>", kruzok)
window.mainloop()