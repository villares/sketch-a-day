# Some ideas from:
# https://forum.processing.org/two/discussion/20499/moving-a-translucent-window-around-the-screen/p1

import py5
from javax.swing import JRootPane

drag = None

def setup():
    global surface, f
    py5.size(500, 500)
    py5.window_resizable(True)

    surface = py5.get_surface()
    f = surface.get_native().getFrame()
    f.removeNotify()
    f.setUndecorated(True)
    f.addNotify()
    #f.getRootPane().setWindowDecorationStyle(JRootPane.FRAME) # .NONE
    f.setOpacity(0.5)

def draw():
    #py5.background(255, 0, 0)
    py5.circle(py5.width / 2, py5.height / 2, py5.width)
    py5.window_x = py5.mouse_x

def mouse_pressed():
    global drag
    drag = True

def mouse_dragged():
    if drag:
        dx = int((py5.mouse_x - py5.pmouse_x) * 0.90)
        dy = int((py5.mouse_y - py5.pmouse_y) * 0.90)
        py5.window_move( f.location().x + dx,  f.location().y + dy)
        
def mouse_released():
    global drag
    drag = False
    
py5.run_sketch(block=False)