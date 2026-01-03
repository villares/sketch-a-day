"""
Press the mouse to see the handles and reshape the quads
"""

import py5
import py5_tools
import numpy as np

drag = None
W, H = 50, 50
M = 50
PTS = np.array([
    np.array((M - W, M - H)),     
    np.array((M + W, M - H)),     
    np.array((M + W, M + H)),     
    np.array((M - W, M + H)),     
])
pts = PTS.copy()
t0 = None


def setup():
    py5.size(600, 600)
 
def draw():
    py5.background(0)
    py5.no_fill() 
    py5.stroke_weight(2)
    py5.stroke(255)
    py5.translate(py5.width / 2, py5.height / 2)
    if t0 is not None:
        t = sigmoid_easing(py5.remap(py5.frame_count, t0, t0 + 360, 0, 1))
    else:
        t = 1
    for a in range(0, 360, 18): 
        angle = py5.radians(a) * t
        R = np.array(((np.cos(angle), -np.sin(angle)),
                      (np.sin(angle),  np.cos(angle))))
        result = pts @ R        
        with py5.begin_closed_shape():
             py5.vertices(result)
    py5.stroke_weight(10)
    for x, y in pts:
        if mouse_over(x, y) or py5.is_mouse_pressed:
            py5.stroke(200, 200, 0)
            py5.point(x, y)
  
  
def sigmoid_easing(p, const=6):  
    """ from John @introscopia """
    m = py5.lerp(-const, const, p)
    return 1 / (1 + np.exp(-m))

def mouse_over(x, y, radius=10):
    return py5.dist(
        x, y, py5.mouse_x - py5.width / 2, py5.mouse_y - py5.height / 2) < radius
  
def mouse_pressed():
    global drag
    if drag is None:
        for i, (x, y) in enumerate(pts):
            if mouse_over(x, y):
                drag = i
                break
            
def mouse_dragged():
    if drag is not None:
        m = np.array((py5.mouse_x, py5.mouse_y))
        pm = np.array((py5.pmouse_x, py5.pmouse_y))
        delta =  m - pm 
        pts[drag] += delta 
    
def mouse_released():
    global drag
    drag = None
     
def key_pressed():
    global t0
    if py5.key == ' ':
        pts[:] = PTS
    elif py5.key == 's':
        py5.save_frame('out.png')
    elif py5.key == 'r':
        t0 = py5.frame_count + 1
        py5_tools.animated_gif(
        f'out{t0}.gif',
        frame_numbers=range(t0, t0 + 360, 6),
        duration=0.15
   )
     
py5.run_sketch(block=False)

