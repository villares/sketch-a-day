from itertools import product
import numpy as np
import py5
import shapely

def setup():
    global out
    py5.size(1000, 900)
    grade = list(product(
        range(-450, 451, 100), range(-400, 401, 100)))
    n = len(grade)  # numero total de estrelas
    ws = np.linspace(20, 40, n)
    hs = np.linspace(70, 0, n)
    py5.translate(py5.width / 2, py5.height / 2)
    py5.background(0)
    py5.no_stroke()
    for (x, y), w, h in zip(grade, ws, hs):
        py5.fill(h * 5, abs(y / 2), w * 5)
        p = py5.random_choice((4, 5, 6, 7, 8, 9))
        py5.shape(estrela(x, y, p, w, h, buffer=x/100, rot=0))  
    py5.save_frame('out.png')
    
def estrela(x, y, n, ra, rb, buffer=0, rot=0):    
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
    e  = shapely.Polygon(vs).buffer(buffer)
    return e - e.buffer(-4) #.buffer(-1)

py5.run_sketch()