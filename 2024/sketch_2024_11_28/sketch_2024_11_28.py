from collections import deque
import py5

history = deque(maxlen=200)

def setup():
    py5.size(500, 500)
    py5.color_mode(py5.HSB)
  
def draw():
    py5.background('blue')
    for i, (x, y, d) in enumerate(history):
        py5.fill(d * 2.5,
                 255, 255, 100)
        td = d + d * py5.sin(i/20)
        py5.circle(x, y, td)
    if history:
        history.append(history.popleft())
    
    
def key_pressed():
    if py5.key == 's':
        py5.save_frame('####.png')
    
def mouse_dragged():
    d = py5.random(20, 40)
    history.append(
        (py5.mouse_x, py5.mouse_y, d)
        )
    
py5.run_sketch()