import py5
import numpy as np

vs = []
shapes = []

def setup():
    py5.size(800, 800)
    start()
    
def start():
    vs[:] = (
        np.array(pt) for pt in
        ((0, 0), (py5.width, 0), (py5.width, py5.height), (0, py5.height))
    )
    shapes.clear()
    shapes.append(np.array((0, 1, 2, 3)))
    
def draw():
    py5.background(0)
    py5.no_fill()
    py5.stroke(255)
    for shp in shapes:
        with py5.begin_closed_shape():
            py5.vertices(np.array(vs)[shp])

def split_shapes():
    new_shapes = []
    while shapes:
        shp = shapes.pop()
        if len(shp) == 4:
            a, b, c, d = shp
            new_shapes.append(np.array((a, b, c)))
            new_shapes.append(np.array((a, c, d)))
        elif py5.random(100) < 50:
            a, b, c = shp
            ab = py5.dist(*vs[a], *vs[b])
            bc = py5.dist(*vs[b], *vs[c])
            i = len(vs)
            if ab > bc:
                vs.append((vs[a] + vs[b]) / 2)
                new_shapes.append(np.array((a, i, c)))
                new_shapes.append(np.array((i, b, c)))
            elif bc > ab:
                vs.append((vs[b] + vs[c]) / 2)
                new_shapes.append(np.array((b, i, a)))
                new_shapes.append(np.array((i, c, a)))                
            else:
                vs.append((vs[a] + vs[c]) / 2)
                new_shapes.append(np.array((a, i, b)))
                new_shapes.append(np.array((i, c, b)))
        else:
            new_shapes.append(shp)

    shapes[:] = new_shapes        

def key_pressed():
    if py5.key == ' ':
        split_shapes()
        print(shapes)
    elif py5.key == 'r':
        start()
    elif py5.key == 'p':
        py5.save_frame('###.png')
        
py5.run_sketch()