import py5
# Wolfram's cellular automata + some color
# Inspired by something made by Carlos @vamoss a long time ago.

from random import choice
import numpy as np
import py5

rows = cols = 200
scale_factor = 4

def setup():
    py5.size(800, 800)
    py5.no_smooth()
    #py5.stroke_cap(py5.PROJECT)
    py5.stroke_weight(scale_factor)    
    start()

def start():
    global matrix, gen, ruleset
    matrix = np.zeros((cols, rows), dtype=int)
    matrix[cols // 2, 0] = 1 # Starts with "1" in the middle of the first line
    matrix[:, 0] = [choice((0, 1)) for _ in range(cols)]
    gen = 0
    #ruleset = np.array([1, 0, 1, 0, 1, 1, 1, 0])
    #print(ruleset)
    for r in range(rows):
        if r % 20 == 0:
            ruleset = np.array([choice((0, 1)) for _ in range(8)])
        new_gen()

def draw():
    py5.background(0)
    offset = gen % rows
    for i in range(cols):
        for j in range(rows):
            y = j - offset
            if y <= 0:
                y = rows + y
            if matrix[i, j] == 1:  # Se a célula i, está viva/ativa/1
                left = matrix[(i + cols - 1) % cols, j - 1]
                centre = matrix[i, j - 1]
                right = matrix[(i + 1) % cols, j - 1]
                c = py5.color(55 + left * 100, 55 + centre * 100, 55 + right * 100)
                py5.stroke(c) 
            else:
                py5.stroke(0)
            py5.point((i + 0.5) * scale_factor , (y - 0.5) * scale_factor)
    
    
def new_gen():
    global gen
    current_row = matrix[:, gen % rows]
    left = np.roll(current_row, 1)
    right = np.roll(current_row, -1)
    rule_idx = (left << 2) + (current_row << 1) + right
    matrix[:, (gen + 1) % rows] = ruleset[rule_idx]
    gen += 1
    
def key_pressed():
    if py5.key == ' ':
        start()
    else:
        py5.save_frame(f'###.png')

py5.run_sketch(block=False)