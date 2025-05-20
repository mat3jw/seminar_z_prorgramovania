from tkinter import *
from random import *

okno = Tk()
WIDTH, HEIGHT = 600, 600
canvas = Canvas(okno, width=WIDTH, height=HEIGHT, bg="black")
canvas.pack()

def draw_chess_board():
    square_size = min(WIDTH, HEIGHT) // 8
    for row in range(8):
        for col in range(8):
            x1 = col * square_size
            y1 = row * square_size
            x2 = x1 + square_size
            y2 = y1 + square_size
            color = "white" if (row + col) % 2 == 0 else "black"
            canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline=color)
            text_color = "black" if color == "white" else "white"
            if col == 0:
                canvas.create_text(x1 + square_size // 4, y1 + square_size // 2, text=str(8 - row), fill=text_color, font=("Arial", 12))
            if row == 7:
                canvas.create_text(x1 + square_size // 2, y2 - square_size // 8, text=chr(65 + col), fill=text_color, font=("Arial", 12))

draw_chess_board()

okno.mainloop()
