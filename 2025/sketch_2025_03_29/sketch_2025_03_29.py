# with help from John @introscopia

import py5

T = {'x': 0, 'y': 0, 'scale': 1, 'i': 0}

def setup():
    py5.size(500, 500)
    
def draw():  
    py5.translate(T['x'], T['y'])
    py5.scale(T['scale'])
    py5.background(0)
    py5.random_seed(1)
    for d in range(250, 5, -5):
        py5.fill(py5.random(255),py5.random(255),py5.random(255))
        py5.circle(250, 250, d)
    
def mouse_wheel(e):
    xrd = (py5.mouse_x - T['x']) / T['scale']
    yrd = (py5.mouse_y - T['y']) / T['scale']
    T['i'] -= e.get_count()
    print(e.get_count())
    T['scale'] = pow(1.1, T['i'])
    T['x'] = py5.mouse_x - xrd * T['scale']
    T['y'] = py5.mouse_y - yrd * T['scale']

def mouse_dragged():
    T['x'] += py5.mouse_x - py5.pmouse_x
    T['y'] += py5.mouse_y - py5.pmouse_y

py5.run_sketch()
