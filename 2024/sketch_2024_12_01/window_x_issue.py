import py5

def setup():
    global surface, f
    py5.size(500, 500)
    surface = py5.get_surface()
    f = surface.get_native().getFrame()

def draw():
    py5.circle(py5.width / 2, py5.height / 2, py5.width)

def mouse_pressed():
    global drag
    drag = True

def mouse_dragged():
    if drag:
        dx = int((py5.mouse_x - py5.pmouse_x) * 2)
        dy = int((py5.mouse_y - py5.pmouse_y) * 2)
        #I should be able to use py5.window_x and _y but it didn't work well
        py5.window_move(py5.window_x + dx,  py5.window_y + dy)
        #py5.window_move(f.location().x + dx,  f.location().y + dy)
        # If you drag around the window by the canvas you get a mismatch:
        print(f.location().x, f.location().y, py5.window_x, py5.window_y)
        
def mouse_released():
    global drag
    drag = False
    
py5.run_sketch(block=False)