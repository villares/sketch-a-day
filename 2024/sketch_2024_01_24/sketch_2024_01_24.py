import py5
import py5_tools

rx = 145
ry = -135

def setup():
    py5.size(400, 400, py5.P3D)
#    py5_tools.animated_gif('out.gif', count=120, period=0.1, duration=0.1)

def draw():
    py5.background('black')
    py5.lights()
    py5.ortho()
    py5.translate(300, 200)
    py5.scale(2)
    py5.rotate_x(py5.radians(rx))
    py5.rotate_y(py5.radians(ry))
    py5.stroke(255)
    b(50, -50, 0)
    py5.line(50, -50, 0, 50, 0, 0)
    b(50, 0, 0)
    py5.line(50, 0, 50, 50, 0, 0)
    b(50, 0, 50)
    py5.line(50, 0, 50, 0, 0, 50)
    #b(0, 0, 50)
 
 
def b(x, y, z, w=20, h=20, d=20):
    with py5.push_matrix():
        py5.translate(x, y, z)
        py5.box(w, h, d)
 
def key_pressed():
    global rx, ry
    kc, UP, DOWN, LEFT, RIGHT = py5.key_code, py5.UP, py5.DOWN, py5.LEFT, py5.RIGHT
    
    if kc == UP:
        rx += 5
    elif kc == DOWN:
        rx -= 5
    elif kc == LEFT:
        ry += 5
    elif kc == RIGHT:
        ry -= 5
    print(rx, ry)
    py5.save('out.png')
 
py5.run_sketch()