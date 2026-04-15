from tkinter import *
from random import *

letters = "ABCDEFGHIJKL"
stvorcekov = len(letters)
sirka = 50
medzera = 20

vyhra = choice(letters)

sirka_okna = stvorcekov * sirka + (stvorcekov + 1) * medzera
vyska_okna = sirka + 2 * medzera

window = Tk()
canvas = Canvas(window, width=sirka_okna, height=vyska_okna)
canvas.pack()

x,y = medzera, medzera
for i in range(stvorcekov):
    tagy = ''
    if letters[i] == vyhra:
        tagy = "vyherny_stvorec"

    canvas.create_rectangle(x, y, x + sirka, y + sirka, fill="green", tags=tagy)
    canvas.create_text(x + sirka / 2, y + sirka / 2, text=letters[i], font=("Arial", 20), tags=tagy)
    x += sirka + medzera

def kruzok(suradnice):
    canvas.delete("all")
    canvas.create_text(sirka_okna / 2, vyska_okna / 2, text="Vyhral si!")
    utvar = canvas.find.withtag("current")
    canvas.itemconfig(utvar, fill="red")

canvas.tag_bind("vyherny_stvorec", "<Button-1>", kruzok)
window.mainloop()  