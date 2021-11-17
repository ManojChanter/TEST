from tkinter import *
import math
import random

root = Tk(className='Barsnley Fern')

c_width = 800
c_height = 800
canvas = Canvas(height=c_height, width=c_width, bg='#fffaf6')


def scale_up_drawing(start_x, start_y, x, y):
    drawn_x = math.floor(start_x + x * c_width / 11)
    drawn_y = math.floor(start_y - y * c_height / 11)
    return drawn_x, drawn_y


def draw_barnsley_fern(accuracy):

    a, b, c, d, e, f, x, y = 0, 0, 0, 0, 0, 0, 0, 0

    start_x = c_width / 2
    start_y = c_height

    for i in range(accuracy):
        random_num = random.randint(0, 100)/100
        if random_num <= 0.01:
            a, b, c, d, e, f = 0, 0, 0, 0.16, 0, 0
        elif random_num <= 0.86:
            a, b, c, d, e, f = 0.85, 0.04, -0.04, 0.85, 0, 1.60
        elif random_num <= 0.93:
            a, b, c, d, e, f = 0.20, -0.26, 0.23, 0.22, 0, 1.60
        else:
            a, b, c, d, e, f = -0.15, 0.28, 0.26, 0.24, 0, 0.44

        new_x = a * x + b * y + e
        new_y = c * x + d * y + f

        x = new_x
        y = new_y

        drawn_x, drawn_y = scale_up_drawing(start_x, start_y, x, y)
        canvas.create_rectangle(drawn_x, drawn_y, drawn_x + 1, drawn_y - 1, outline='#218f4d')


draw_barnsley_fern(150000)
canvas.pack()
root.mainloop()