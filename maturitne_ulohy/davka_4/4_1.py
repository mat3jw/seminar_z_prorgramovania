from tkinter import *
from random import *

letters = "ABCDEFGHIJKL"
stvorcekov = len(letters)
sirka = 50
medzera = 20

sirka_okna = stvorcekov * sirka + (stvorcekov + 1) * medzera
vyska_okna = sirka + 2 * medzera

window = Tk()
canvas = Canvas(window, width=sirka_okna, height=vyska_okna)
canvas.pack()

x,y = medzera, medzera
for i in range(stvorcekov):
    farba = "#%06x" % randint(0, 0xFFFFFF)
    canvas.create_rectangle(x, y, x + sirka, y + sirka, fill=farba)
    canvas.create_text(x + sirka / 2, y + sirka / 2, text=letters[i], font=("Arial", 20))
    x += sirka + medzera