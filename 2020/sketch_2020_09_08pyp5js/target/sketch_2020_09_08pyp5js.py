from pyp5js import *
from random import shuffle

add_library("p5.dom.js")

seed_value = 1
sf = 1

gliphs = [lambda x, y, s: rect(x, y, s, s),
          lambda x, y, s: ellipse(x, y, s, s),
          lambda x, y, s: triangle(x - s, y, x - s, y + s, x, y + s),
          lambda x, y, s: triangle(x + s, y, x + s, y - s, x, y - s),
          ]

colors = ((0, 50, 50, 150),
          (200, 0, 0, 150)
          )

checkbox = None

def setup():
    createCanvas(1200, 600)
    global checkbox
    checkbox = createCheckbox('auto-update', False);
    checkbox.changed(cb_changed)
    # checkbox.position(10, 10)
    checkbox.value = False

def draw():
    randomSeed(seed_value)
    background(240, 240, 240)
    grid(width / 2, height / 2, (8, 4), 150 * sf, ensamble, 5)

    if checkbox.value and frameCount % 60 == 0: shuffle(gliphs)

def keyPressed():
    global seed_value
    seed_value = mouseX + (1000 * mouseY)
    
def cb_changed():
    checkbox.value = not checkbox.value
    
    
def ensamble(ex, ey, eo):
    noStroke()
    for i in range(eo):
        fill(colors[i % len(colors)])
        order, spacing, side = int(random(3, 7)), 14, 7
        x = (1 + int(random(-5, 5))) * side * sf
        y = (1 + int(random(-5, 5))) * side * sf
        grid(ex+x,
             ey+y,
             order,
             spacing * sf,
             gliphs[int(random(len(gliphs)))],
             side * sf)
             
def grid(x, y, order, spacing, func, args):  
    if type(order) is tuple:
        cols, rows = order
    else:
        cols = rows = order
    xo, yo = x - cols * spacing / 2 , y - rows * spacing / 2
    for i in range(cols):
        gx = spacing / 2 + i * spacing
        for j in range(rows):
            gy = spacing/2 + j * spacing
            func(xo + gx, yo + gy, args)