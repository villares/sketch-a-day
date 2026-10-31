from itertools import product
import numpy as np
import py5
import shapely

def setup():
    global out
    py5.size(1000, 900)
    grade = sorted(list(np.random.random((100, 2)) * 800 - 400),
                   key=lambda k:k[1],
                   #reverse=True
                   )
    n = len(grade)  # numero total de estrelas
    ws = np.linspace(20, 40, n)
    hs = np.linspace(70, 0, n)
    py5.translate(py5.width / 2, py5.height / 2)
    py5.background(0)
    py5.no_stroke()
    for (x, y), w, h in zip(grade, ws, hs):
        py5.fill(h * 5, abs(y / 2), w * 5)
        p = py5.random_choice((4, 5, 6, 7, 8, 9))
        for i in range(5):
             e = estrela(x, y, p, w, h,
                         buffer=x/100,
                         hole=1 + abs(y/20))
             py5.shape(e)
    py5.save_frame('out.png')
    
def estrela(x, y, n, ra, rb, buffer=0, hole=1, rot=0):    
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
    return e - e.buffer(-hole) #.buffer(-1)

py5.run_sketch()