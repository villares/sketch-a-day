import py5
import shapely

star_data = [
    {'x': 400, 'y': 100, 'n': 5, 'ra': 50, 'rb': 10, 'buffer': 0},
    {'x': 200, 'y': 200, 'n': 7, 'ra': 150,'rb': 100,'buffer': 0},
    {'x': 350, 'y': 400, 'n': 20,'ra': 80, 'rb': 40, 'buffer': 0},
]
picked_star = None

def setup():
    py5.size(500, 500)
    
def draw():
    global under_mouse
    py5.background(0)
    under_mouse = None
    for i, sd in enumerate(star_data):
        shp = star(**sd)
        py5.no_stroke()
        if shp.contains(shapely.Point(py5.mouse_x, py5.mouse_y)):
            under_mouse = i
            py5.stroke(255, 0, 0)
        py5.shape(shp)
          
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
    
def mouse_pressed():
    global picked_star
    picked_star = under_mouse
    
def mouse_dragged():
    if picked_star is not None:
        sd = star_data[picked_star]
        sd['x'] += py5.mouse_x - py5.pmouse_x
        sd['y'] += py5.mouse_y - py5.pmouse_y

def mouse_released():
    global picked_star
    picked_star = None
    
def mouse_wheel(e):
    if under_mouse is not None:
        sd = star_data[under_mouse]
        if e.is_control_down():
            sd['buffer'] += e.get_count()
        elif e.is_shift_down():
            sd['rb'] += e.get_count()
        else:
            sd['ra'] += e.get_count()
 

def key_pressed():
    if py5.key == 'p':
        py5.save_frame('out.png')
    elif py5.key == 's':
        star_data.append(
            {'x': py5.mouse_x, 'y': py5.mouse_y,
             'n': 4, 'ra': 50, 'rb': 10, 'buffer': 0},
            )

py5.run_sketch(block=False)
        
        
    
    
    
