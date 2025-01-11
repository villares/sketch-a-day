# Wolfram's cellular automata + some color
# Inspired by something made by Carlos @vamoss a long time ago.

import numpy as np
import py5

rows = cols = 100
matrix = np.zeros((100, 100), dtype=int) 

nice_rules = [    # Some rules we like
    [1, 0, 1, 1, 1, 1, 1, 0],  # rule 125
    [1, 0, 0, 1, 0, 1, 0, 1],  # rule 169
    [0, 1, 1, 1, 1, 0, 0, 0],  # rule 30
    [0, 1, 1, 1, 0, 1, 1, 0],  # rule 110
]
ruleset = nice_rules[2]
gen = 0

def setup():
    py5.size(800, 800)
    py5.no_smooth()
    matrix[cols // 2, 0] = 1 # Starts with "1" in the middle of the first line
    py5.frame_rate(10)

def draw():
    py5.background(200)
    py5.scale(8)
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
                py5.stroke(200)
            py5.point(i, y - 1)
    new_gen()

def new_gen():
    global gen
    for i in range(cols):
        left = matrix[(i + cols - 1) % cols, gen % rows]
        centre = matrix[i, gen % rows]
        right = matrix[(i + 1) % cols, gen % rows]
        result = ruleset[left  * 4 +  centre * 2 +  right * 1]
        matrix[i, (gen + 1) % rows] =  result 
    gen += 1
    
def key_pressed():
    py5.save_frame('####.png')

py5.run_sketch()
