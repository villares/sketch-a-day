gestures = [[]]
z = ax = ay = 0

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
        for x, y, z, rx, ry in gesture:
            fx, fy, fz = get_rotated_point(x, y, z, rx, ry)
            stroke(abs(z), 255, 128)
            noFill()
            vertex(fx, fy, fz)
            
def get_rotated_point(x, y, z, rx, ry):
    with pushMatrix():
        translate(width / 2, height / 2)
        rotateY(radians(ry - ay)) 
        rotateX(radians(rx - ax)) 
        translate(-width / 2, -height / 2)
        translate(x, y, z)
        return modelX(0, 0, 0), modelY(0, 0, 0), modelZ(0, 0, 0)            

def mouseDragged():
    global ax, ay
    if mouseButton == LEFT:
        gestures[-1].append((mouseX, mouseY, z, ax, ay))
    else:
        dx = mouseX - pmouseX
        ay += dx
        dy = mouseY - pmouseY
        ax += dy
    
def mouseReleased():
    gestures.append([])
    
def keyPressed():
    global z, ax, ay
    if key == 'a':
        z += 10
    elif key == 'z':
        z -= 10
    elif key == ' ':
        ax = ay = 0
