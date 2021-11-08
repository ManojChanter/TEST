from tkinter import *
root = Tk(className='My Pen')
title = StringVar()
title.set('my first canvas drawing')
label = Label(root, textvariable=title)
label.pack()
c_width = 500
c_height = 500
canvas = Canvas(root, width=c_width, height=c_height, bg='lightblue')
blue_line = canvas.create_line(20, 240, 240, 500)
canvas.create_line(20, 240, 240, 20)
canvas.create_rectangle(10, 10, 0.5*c_width-20, 0.5*c_height-10)
canvas.create_polygon(600, 400, 650, 200, 800, 100)
canvas.create_oval(200, 600, 350, 700)

# coord = c_width/2, c_height/2, c_width, c_height
# canvas.create_arc(coord, start=10, extent =140)

"""
print('convert 150:')
print(hex(150))
print(hex(150) [2:1])
print('convert 1:')
print(hex(1))
print(hex(1)[2:1])
print('%02x' % 1)

def convert_rgb_to_hex(red, green, blue):
    return '#%02x%02x%02x' % (red, green, blue)
print(convert_rgb_to_hex(0,255, 255))
yellow = convert_rgb_to_hex(150, 150, 0)

x1 = 0
y1 = 0
x2 = c_width
y2 = c_height
colors =['blue', 'red', 'lightblue', 'green', 'black', 'salmon']
for i in range(10):
    canvas.create_rectangle(x1, y1, x2, y2)
    x1 += 20
    y1 += 20
    x2 -=20
    y2 -=20







"""
canvas.pack()
root.mainloop()