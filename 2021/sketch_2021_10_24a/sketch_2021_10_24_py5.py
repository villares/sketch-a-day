gestures = [[]]
z = ax = ay = 0

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
        for x, y, z, rx, ry in gesture:
            fx, fy, fz = get_rotated_point(x, y, z, rx, ry)
            stroke(abs(z), 255, 128)
            no_fill()
            vertex(fx, fy, fz)
            
def get_rotated_point(x, y, z, rx, ry):
    with push_matrix():
        translate(width / 2, height / 2)
        rotate_y(radians(ry - ay)) 
        rotate_x(radians(rx - ax)) 
        translate(-width / 2, -height / 2)
        translate(x, y, z)
        return model_x(0, 0, 0), model_y(0, 0, 0), model_z(0, 0, 0)            

def mouse_dragged():
    global ax, ay
    if mouse_button == LEFT:
        gestures[-1].append((mouse_x, mouse_y, z, ax, ay))
    else:
        dx = mouse_x - pmouse_x
        ay += dx
        dy = mouse_y - pmouse_y
        ax += dy
    
            
def mouse_released():
    gestures.append([])
    
def key_pressed():
    global z, ax, ay
    if key == 'a':
        z += 10
    elif key == 'z':
        z -= 10
    elif key == ' ':
        ax = ay = 0
