x = -400
y = -400
xv, yv = -1, -1

def setup():
    size(600, 400)
    global img 
    img = loadImage("P1030601.JPG")
    # img = loadImage("P1030634.JPG")
    frameRate(30)
    noSmooth()
    
def draw():
    global x, y, xv, yv
    background(0)
    step = 4
    strokeWeight(3)
    for i in range(0, width, step):
        for j in range(0, height, step):
            if inside_img(i - x, j - y, img):
                c = img.get(i - x, j - y)
                stroke(c)
                point(i,j)
    # image(img, x, y)
    x = int(x + xv)
    y = int(y + yv)
    if x < -img.width + width: xv = -xv
    if x > 0: xv = -xv
    if y < -img.height + height: yv = -yv
    if y > 0: yv = -yv
    print(frameRate, x, y)
    
def inside_img(x, y, img):
    return 0 < x < img.width and 0 < y < img.height

def keyPressed():
    global x, y, xv, xy
    if key == ' ':
        xv = random(-3, 3)
        yv = random(-3, 3)        
