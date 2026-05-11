from tkinter import *

w= 300
h = 500

#0 - hore, 1 - vpravo, 2 - dole, 3 - vlavo
x, y, smer = w//2, h//2, 0

window = Tk()
canvas = Canvas(window, width = w, height = h, bg="#aaaaaa")

canvas.pack()
vstup = Entry()
vstup.pack()

def urob():
    global smer, x, y
    prikaz = vstup.get()
    print(prikaz)
    if prikaz == "vpravo":
        smer = (smer + 1) % 4
    elif prikaz == "vlavo":
        smer = (smer - 1) % 4
    elif prikaz[:5] == "sadit":
        prikaz = prikaz.strip().split()
        if len(prikaz) == 2:
            dlzka = int(prikaz[1])
            nove_x, nove_y = x, y
            if smer == 0:
                nove_y -= dlzka
            elif smer == 1:
                nove_x += dlzka
            elif smer == 2:
                nove_y += dlzka
            elif smer == 3:
                nove_x -= dlzka
            canvas.create_line(x, y, nove_x, nove_y, fill= "green", width = 4)
            x, y = nove_x, nove_y
              

tlacidlo = Button(text= "vykonaj", command= urob)
tlacidlo.pack()



window.mainloop()