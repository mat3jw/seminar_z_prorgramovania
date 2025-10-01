import turtle

t = turtle.Turtle()
t.speed(0)
t.pencolor("white")
screen = turtle.Screen()
screen.bgcolor("black")


def draw_h(t, x, y, size):
    
    t.penup()
    t.goto(x - size/2, y)
    t.pendown()
    t.goto(x + size/2, y)
    
    t.penup()
    t.goto(x - size/2, y + size/2)
    t.pendown()
    t.goto(x - size/2, y - size/2)
    
    t.penup()
    t.goto(x + size/2, y + size/2)
    t.pendown()
    t.goto(x + size/2, y - size/2)

def h_tree(t, x, y, size, depth):
    if depth == 0:
        return
    draw_h(t, x, y, size)
    
    half = size / 2
    h_tree(t, x - half, y + half, half, depth - 1)
    h_tree(t, x - half, y - half, half, depth - 1)
    h_tree(t, x + half, y + half, half, depth - 1)
    h_tree(t, x + half, y - half, half, depth - 1)





h_tree(t, 0, 0, 200, 4)

screen.mainloop()