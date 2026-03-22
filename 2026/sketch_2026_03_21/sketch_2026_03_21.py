import py5
import numpy as np

poly = [(100, 100), (300, 150), (500, 100), (450, 300), (500, 500),
        (300, 450), (100, 500), (150, 300)]

def setup():
    py5.size(600, 600)
    py5.stroke_cap(py5.ROUND)
    
    
def draw():
    py5.background(220, 220, 180)
    es = edges(poly)
    py5.stroke_weight(4)
    py5.stroke(0, 100, 0)
    for i, e in enumerate(es):
        if i % 2:
            dashed_line(*e)
        else:
            dotted_line(*e)
    py5.translate(20, 20)
    py5.stroke_weight(5)
    py5.stroke(0, 100, 100)
    dotted_lines(es, d=30)
    
def edges(poly_points):
    poly_points = np.asarray(poly_points)
    rolled = np.roll(poly_points, -1, axis=0)
    return np.column_stack((poly_points, rolled))

def dashed_line(*args, d=20):
    global dashes
    dim = len(args)//2  # 4 args is 2d, 6 args is 3d 
    a = args[:dim]
    b = args[dim:]
    a = np.array(a)
    b = np.array(b)
    c = py5.dist(*a, *b)
    n = int(c / d)
    t = np.linspace((0, 0), (1, 1), n)
    coords = py5.lerp(a, b, t)
    dashes = edges(coords)[:-1:2]
    py5.lines(dashes)

def dotted_line(*args, d=20):
    dim = len(args)//2  # 4 args is 2d, 6 args is 3d 
    a = args[:dim]
    b = args[dim:]
    a = np.array(a)
    b = np.array(b)
    c = py5.dist(*a, *b)
    n = int(c / d)
    t = np.linspace((0, 0), (1, 1), n)
    coords = py5.lerp(a, b, t)
    py5.points(coords)


def dotted_lines(lines, d=10):
    dim = lines.shape[1]//2
    a = lines[:, :dim]
    b = lines[:, dim:]
    a = np.array(a)
    b = np.array(b)
    c = py5.dist(lines[:, 0], lines[:, 1], lines[:, 2], lines[:, 3])
    ns = (c / d).astype(int)
    for i, n in enumerate(ns):
        t = np.linspace((0, 0), (1, 1), n)
        coords = py5.lerp(a[i], b[i], t)
        py5.points(coords)
 
def key_pressed():
    py5.save_frame('out.png')

 
py5.run_sketch(block=False)
