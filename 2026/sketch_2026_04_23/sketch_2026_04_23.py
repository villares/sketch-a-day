import py5
import shapely

star_data = [
    {'x': 400, 'y': 100, 'n': 5, 'ra': 50, 'rb': 10, 'buffer': 0},
    {'x': 200, 'y': 200, 'n': 7, 'ra': 150,'rb': 100,'buffer': 0},
    {'x': 350, 'y': 400, 'n': 20,'ra': 80, 'rb': 40, 'buffer': 0},
]

def setup():
    py5.size(500, 500)
    
def draw():
    py5.background(0)
    for kwargs in star_data:
        star(**kwargs)

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
    shp = shapely.Polygon(vs).buffer(buffer)
    py5.shape(shp)
    
    
def mouse_wheel(e):
    global e_debug
    e_debug = e
    for d in star_data:
        if py5.dist(d['x'], d['y'], py5.mouse_x, py5.mouse_y) < d['ra']:
            if e.is_control_down():
                d['buffer'] += e.get_count()
            if e.is_shift_down():
                d['rb'] += e.get_count()
            else:
                d['ra'] += e.get_count()
 

py5.run_sketch(block=False)
        
        
    
    
    