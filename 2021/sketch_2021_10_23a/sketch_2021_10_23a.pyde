gestures = [[]]
z = 0
a = 0

def setup():
    size(500, 500, P3D)
    colorMode(HSB)
    
def draw():
    ortho()
    background(200)
    for gesture in gestures:
        strokeWeight(2)
        draw_gesture(gesture)

def draw_gesture(gesture):        
    with beginShape():
        for x, y, z, r in gesture:
            fx, fy, fz = get_rotated_point(x, y, z, r)
            stroke(abs(z), 255, 128)
            noFill()
            vertex(fx, fy, fz)
            
def get_rotated_point(x, y, z, r):
    with pushMatrix():
        translate(width / 2, 0)
        rotateY(radians(r - a))  # a: global current rotation
        translate(-width / 2, 0)
        translate(x, y, z)
        return modelX(0, 0, 0), modelY(0, 0, 0), modelZ(0, 0, 0)            

def mouseDragged():
    gestures[-1].append((mouseX, mouseY, z, a))
    
def mouseReleased():
    gestures.append([])
    
def keyPressed():
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
