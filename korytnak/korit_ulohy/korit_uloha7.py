import tkinter as tk
import random

# Konštanty
WIDTH = 800
HEIGHT = 800
SCALE_STEP = 20  
POINT_COUNT = 1000

def draw_axes(canvas):
    
    center_x = WIDTH // 2
    center_y = HEIGHT // 2

    
    canvas.create_line(0, center_y, WIDTH, center_y, arrow=tk.LAST, width=2)  
    canvas.create_line(center_x, 0, center_x, HEIGHT, arrow=tk.LAST, width=2)  

    
    for x in range(0, WIDTH, SCALE_STEP):
        if x == center_x:
            continue
        canvas.create_line(x, center_y - 5, x, center_y + 5)
        canvas.create_text(x, center_y + 15, text=str((x - center_x) // SCALE_STEP * 20), font=("Arial", 8))

    
    for y in range(0, HEIGHT, SCALE_STEP):
        if y == center_y:
            continue
        canvas.create_line(center_x - 5, y, center_x + 5, y)
        canvas.create_text(center_x + 15, y, text=str((center_y - y) // SCALE_STEP * 20), font=("Arial", 8))


def draw_points(canvas):
    center_x = WIDTH // 2
    center_y = HEIGHT // 2

    for z in range(POINT_COUNT):
        x = random.randint(0, WIDTH)
        y = random.randint(0, HEIGHT)

        
        if x > center_x and y < center_y:
            color = "red"  
        elif x < center_x and y < center_y:
            color = "orange"  
        elif x < center_x and y > center_y:
            color = "blue"  
        else:
            color = "green"  

        canvas.create_oval(x - 2, y - 2, x + 2, y + 2, fill=color, outline=color)

root = tk.Tk()
root.title("Súradnicová os s bodmi")

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="white")
canvas.pack()

draw_axes(canvas)
draw_points(canvas)

root.mainloop()