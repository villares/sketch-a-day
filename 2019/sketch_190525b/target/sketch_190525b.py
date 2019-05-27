# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
# More explorations of lines in grids

from pytop5js import *

num = None
H = None
W = None
line_combos = None

from random import shuffle
from itertools import product, combinations, permutations, combinations_with_replacement
space = 15
position = 0  # initial position


def setup():
    global line_combos, W, H, position, num
    createCanvas(1045, 700)
    width, height = 1045, 700
    frameRate(5)
    rectMode(CENTER)
    strokeWeight(2)
    grid = product(range(-1, 2), repeat=2) # 3X3    
    # all possible lines
    lines = combinations(grid, 2)
    # colect only short lines
    short_lines = []
    for l in lines:
        (x0, y0), (x1, y1) = l[0], l[1]
        if dist(x0, y0, x1, y1) < 3: # short as defined here...
            short_lines.append(l)
    num_short_lines = len(short_lines)
    print("Number of possible lines: {}".format(num_short_lines))
    # main stuff
    line_combos = list(combinations(short_lines, 4))
    shuffle(line_combos)
    num = len(line_combos)
    print(num)
    W, H = (width - space) // space, (height - space) // space
    print((W, H, W * H))


def draw():
    global position
    background(240)
    i = position
    for y in range(H):
        for x in range(W):
            if i < len(line_combos):
                push()
                translate(space + space * x, space + space * y)
                draw_combo(i)
                pop()
                i += 1
    if i < len(line_combos):
        position += W

def draw_combo(n):
    siz = space / 3.
    for i, sl in enumerate(line_combos[n]):
        colorMode(HSB, 255, 255, 255)
        stroke(i * 64, 160, 160)
        (x0, y0), (x1, y1) = sl[0], sl[1]
        line(x0 * siz, y0 * siz, x1 * siz, y1 * siz)

def keyPressed():
    if key == "s":
        saveFrame("####.png")

# ==== This is required by pyp5js to work
# Register your events functions here
event_functions = {"keyPressed" : keyPressed,  }
start_p5(setup, draw, event_functions)