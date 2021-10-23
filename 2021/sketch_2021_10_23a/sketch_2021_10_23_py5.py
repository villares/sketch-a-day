gestures = [[]]
z = 0
a = 0

def setup():
    size(500, 500, P3D)
    color_mode(HSB)
    
def draw():
    ortho()
    background(200)
    for gesture in gestures:
        stroke_weight(2)
        draw_gesture(gesture)

def draw_gesture(gesture):        
    with begin_shape():
        for x, y, z, r in gesture:
            fx, fy, fz = get_rotated_point(x, y, z, r)
            stroke(abs(z), 255, 128)
            no_fill()
            vertex(fx, fy, fz)
            
def get_rotated_point(x, y, z, r):
    with push_matrix():
        translate(width / 2, 0)
        rotate_y(radians(r - a))  # a: global current rotation
        translate(-width / 2, 0)
        translate(x, y, z)
        return model_x(0, 0, 0), model_y(0, 0, 0), model_z(0, 0, 0)            

def mouse_dragged():
    gestures[-1].append((mouse_x, mouse_y, z, a))
    
def mouse_released():
    gestures.append([])
    
def key_pressed():
    global z, a
    if key == 'a':
        z += 10
    elif key == 'z':
        z -= 10
    elif key == 'q':
        a -= 10
    elif key == 'w':
        a += 10
    elif key == ' ':
        a = 0