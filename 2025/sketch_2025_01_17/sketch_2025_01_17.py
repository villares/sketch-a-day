import py5
import numpy as np

walks = 1000

def setup():
    py5.size(800, 800)
    py5.no_loop()
    
def draw():
    py5.background(0)
    py5.stroke_weight(3)
    py5.stroke(255, 64)
    for _ in range(walks):
        draw_walk(350)
    
def draw_walk(steps):
    with py5.push_matrix():
        py5.translate(py5.width / 2, py5.height / 2)    
        for x, y in walk(steps):
            py5.line(0, 0, x, y)
            py5.translate(x, y)
        
def positive_walk(distance):
    if distance < 100:
        first = py5.random((distance))
        return py5.random_choice((
            np.array([(first, 0), (0, distance-first)]),
            np.array([(0, distance-first), (first, 0)])
            ))
    else:
        return np.concat((
            positive_walk(distance / 2),
            positive_walk(distance / 2)
            ))

def walk(distance):
    directions = ((1, 1), (-1, 1), (1, -1), (-1, -1))
    direction = np.array(py5.random_choice(directions))    
    return positive_walk(distance) * direction  

def key_pressed():
    py5.redraw()
    py5.save_frame('###.png')

# def walk(steps):
#     positive_steps = ((0, 1), (1, 0))
#     positive_walk = np.array([py5.random_choice(positive_steps)
#                      for _ in range(steps)])
#     directions = ((1, 1), (-1, 1), (1, -1), (-1, -1))
#     direction = np.array(py5.random_choice(directions))    
#     return positive_walk * direction

py5.run_sketch(block=False)

