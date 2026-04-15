from tkinter import *

with open('kitty.txt') as file:
    prvy_riadok = file.readline().strip()
    sirka, vyska = prvy_riadok.split()
    sirka = int(sirka)
    vyska = int(vyska)

    pixely = file.readlines()

window = Tk()
canvas = Canvas(window, width=sirka, height=vyska)
canvas.pack()

x,y = 0,0
for riadok in pixely:
    riadok = riadok.strip()
    for pixel in riadok:
        canvas.create_rectangle(x,y,x+1,y+1, fill=pixel)




window.mainloop()