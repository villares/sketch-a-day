from itertools import product

import numpy as np
import py5
import shapely

grid_points = list(product(range(-450, 451, 100), range(-400, 401, 100)))
scale_factor = 2

def setup():
    global out
    py5.size(1000, 900)
    n = len(grid_points)
    w = np.linspace(20, 40, n)
    h = np.linspace(80, 0, n)
    star_infos = list(zip(grid_points, w, h))
    out = py5.create_graphics(py5.width * scale_factor, py5.height * scale_factor)
    py5.begin_record(out)
    out.scale(scale_factor)
    py5.translate(py5.width / 2, py5.height / 2)
    py5.background(255)
    py5.no_fill()
    py5.stroke(200, 250, 200)            
    for pos, w, h in star_infos:
        with py5.push_matrix():
            py5.translate(*pos)
            s = star(0, 0, 10, w, h, buffer=pos[0]/100)
            for i in range(-10, 11, 1):
                if i != 0:
                    py5.shape(s.buffer(i * 4))
    py5.stroke(0)
    for pos, w, h in star_infos:
        py5.shape(star(*pos, 10, w, h, buffer=pos[0]/100))
        
    py5.end_record()
    
        
def star(x, y, n, ra, rb, buffer=0, rot=0):    
    passo = py5.TWO_PI / n
    vs = [] 
    for i in range(n): 
        angulo = i * passo + rot
        vx = x + ra * py5.sin(angulo)
        vy = y + ra * py5.cos(angulo)
        vs.append((vx, vy))
        vx = x + rb * py5.sin(angulo + passo / 2)
        vy = y + rb * py5.cos(angulo + passo / 2)
        vs.append((vx, vy)) 
    return shapely.Polygon(vs).buffer(buffer)
    
    
def key_pressed():
    if py5.key == 'h':
        out.save(f'outg-x{scale_factor}.png')
    else:
        py5.save('out-800.png')
    
py5.run_sketch(block=False)

