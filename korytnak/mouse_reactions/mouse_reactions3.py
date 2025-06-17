import tkinter as tk

def draw_line(event):
    
    x_center = canvas.winfo_width() // 2
    y_bottom = canvas.winfo_height()
    
    
    canvas.create_line(x_center, y_bottom, event.x, event.y, fill="green", width=5)


okno = tk.Tk()


canvas = tk.Canvas(okno, width=800, height=600, bg="white")
canvas.pack(fill=tk.BOTH, expand=True)


canvas.bind("<Button-1>", draw_line)


okno.mainloop()