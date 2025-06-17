import tkinter as tk

def draw_smiley(event):
    x, y = event.x, event.y

    canvas.create_oval(x - 50, y - 50, x + 50, y + 50, fill="yellow", outline="black")

    canvas.create_oval(x - 20, y - 20, x - 10, y - 10, fill="black")
    canvas.create_oval(x + 10, y - 20, x + 20, y - 10, fill="black")

    canvas.create_arc(x - 30, y - 30, x + 30, y + 30, start=200, extent=140, fill="black", style=tk.CHORD)


okno = tk.Tk()

canvas = tk.Canvas(okno, width=800, height=600, bg="white")
canvas.pack()


canvas.bind("<Button-1>", draw_smiley)


okno.mainloop()