
gesture = []
z = 0
a = 0

def setup():
    size(500, 500, P3D)
    colorMode(HSB)
    
def draw():
    ortho()
    background(200)
    for x, y, z, r in gesture:
        push()
        translate(width / 2, 0)
        rotateY(radians(r - a))
        translate(-width / 2, 0)
        translate(x, y, z)
        fill(abs(z), 255, 128)
        noStroke()
        circle(0, 0, 5)
        pop()
        
def mouseDragged():
    gesture.append((mouseX, mouseY, z, a))
    
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
