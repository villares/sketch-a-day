rot = 0 

def setup():
    size(500, 500)
    # The image file must be in the data folder of
    # the current sketch to load successfully.
    global img
    img = loadImage("moonwalk.jpg")    # Load the image into the programr
        
def draw():
    background(255)
    image(img, 0, height / 4, img.width / 2, img.height / 2)
    image_rot(img, rot, height /2, width / 2, img.width / 4, img.height / 4) 

def image_rot(img, rot, x, y, w=None, h=None):
    w = w or img.width
    h = h or img.height
    pushMatrix()
    if rot == 0:
        image(img, x, y, w, h)
    if rot == 1:
        translate(x + h, y)
        rotate(HALF_PI)
        image(img, 0, 0, w, h)
    if rot == 2:
        translate(x + w, y + h)
        rotate(PI)
        image(img, 0, 0, w, h)    
    if rot == 3:
        translate(x, y + w)
        rotate(HALF_PI + PI)
        image(img, 0, 0, w, h)    
    popMatrix()      
    
def rotate_image(img):    
    rot = createGraphics(img.height, img.width)
    rot.beginDraw()
    rot.imageMode(CENTER)
    rot.translate(img.height / 2, img.width / 2)
    rot.rotate(HALF_PI)
    rot.image(img, 0, 0)
    rot.endDraw()
    return rot

def keyPressed():
    global img, rot
    if key == 'r':
        img = rotate_image(img)
    if key == ' ':
        rot = (rot + 1) % 4
