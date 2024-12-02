import py5

drag = None

def setup():
    global surface, f
    py5.size(500, 500)
    #py5.window_resizable(True)
    surface = py5.get_surface()
    f = surface.get_native().getFrame()
    f.removeNotify()
    f.setUndecorated(True)
    f.setOpacity(0.5)
    f.addNotify()
    
def draw():
    #py5.background(255, 0, 0)
    py5.circle(py5.width / 2, py5.height / 2, py5.width)
    py5.window_x = py5.mouse_x

def mouse_pressed():
    global drag
    drag = py5.mouse_x, py5.mouse_y, py5.window_x, py5.window_y
        
def mouse_released():
    global drag
    if drag:
        px, py, wx, wy = drag
        dx = py5.pmouse_x - px
        dy = py5.pmouse_y - py
        surface.set_location(wx + dx , wy + dy)
        drag = None
    
py5.run_sketch(block=False)