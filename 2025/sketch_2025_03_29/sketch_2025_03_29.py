# with help from John @introscopia

import py5

T = {'x': 0, 'y': 0, 'scale': 1, 'i': 0}
seed = 1

def setup():
    py5.size(500, 500)
    py5.no_stroke()
    
def draw():  
    py5.translate(T['x'], T['y'])
    py5.scale(T['scale'])
    py5.background(0)
    py5.random_seed(seed)
    w = 500
    for _ in range(10):
        x, y = py5.random(-w/2, w + w/2), py5.random(-w/2, w + w/2)
        for d in range(w * 2, 0, -10):
            py5.fill(py5.random(255),py5.random(255),py5.random(255), 50)
            py5.circle(x, y, d)
    
def mouse_wheel(e):
    xrd = (py5.mouse_x - T['x']) / T['scale']
    yrd = (py5.mouse_y - T['y']) / T['scale']
    T['i'] -= e.get_count()
    T['scale'] = 1.1 ** T['i']
    T['x'] = py5.mouse_x - xrd * T['scale']
    T['y'] = py5.mouse_y - yrd * T['scale']

def mouse_dragged():
    T['x'] += py5.mouse_x - py5.pmouse_x
    T['y'] += py5.mouse_y - py5.pmouse_y

def key_pressed():
    global seed
    seed += 1

py5.run_sketch()
