from tkinter import *
import random
root = Tk(className="Barsnley Fern")
c_width = 800
c_height = 800
canvas = Canvas(width=c_width, height=c_height, bg='#fffaf6')
def scale_up_drawing(start_x, start_y, x, y):
    draw_x = start_x + x * 75
    draw_y = start_y - y * 75
    return draw_x, draw_y

def draw_barsnley_fern():
    a, b, c, d, e, f, x, y = 0, 0, 0, 0, 0, 0, 0, 0
    start_x = c_width/2
    start_y = c_height
    for i in range(100000):
        rand = random.randint(0, 100)/100
        if rand <= 0.01:
            a, b, c, d, e, f = 0, 0, 0, 0.16, 0, 0
        elif rand <= 0.86:
            a, b, c, d, e, f = 0.85, 0.04, -0.04, 0.85, 0, 1.60
        elif rand <= 0.93:
            a, b, c, d, e, f = 0.20, -0.26, 0.23, 0.22, 0, 1.6
        else:
            a, b, c, d, e, f = -0.15, 0.28, 0.26, 0.24, 0, 0.44
        new_x = a * x + b * y + e
        new_y = c * x + y * d + f
        x = new_x
        y = new_y
        draw_x, draw_y = scale_up_drawing(start_x, start_y, x, y)
        canvas.create_rectangle(draw_x, draw_y, draw_x + 1, draw_y - 1, outline='#218f4d')
draw_barsnley_fern()
canvas.pack()
root.mainloop()