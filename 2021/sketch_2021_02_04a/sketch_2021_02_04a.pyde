# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
SKETCH_NAME = "2021_01_04" # based on "s279"  # 20181004
OUTPUT = ".gif"

add_library('peasycam')
from random import seed
from random import choice
from random import randint

rnd_seed = 1000

def setup():
    size(600, 600, P3D)
    #smooth()
    rectMode(CENTER)
    colorMode(HSB)
    fill(0)
    textMode(SHAPE)
    
    cam = PeasyCam(this, 400)
    f = createFont("Tomorrow Bold", 14)
    textFont(f)
    textSize(14)
    global mi, ma
    mi, ma = 5, 10


def draw():
    #noLoop()
    background(200) 
    random_seed()
    translate(0, 0, -100)
    ensamble(0, 0, 5)
    translate(0, 0, 200)
    ensamble(0, 0, 5)
    translate(0, 0, -100)
    rotateX(HALF_PI)
    translate(0, 0, -100)
    ensamble(0, 0, 5)
    translate(0, 0, 200)
    ensamble(0, 0, 5)
    translate(0, 0, -100)
 
    # ensamble(width/2, height/2, 5)


def ensamble(ex, ey, order):
    with pushMatrix():
        translate(ex, ey)
        # #rotate(QUARTER_PI)
        gliph = lambda x, y, l: text(l, x, y)
        for _ in range(order): 
            # rotate(QUARTER_PI)
            order = randint(mi, ma)
            spacing, side = 14, 14
            x, y = int(random(-5, 5)) * side, int(random(-5, 5)) * side 
            #fill(randint(1 , 5) * 48, 255, 255) # H, S, B
            # grid(x, y, order, spacing, gliph, c)
            colorMode(HSB)
            fill(x % 255, 255, 255)
            push()
            # translate(x - order * spacing / 2, y- order * spacing / 2)
            face(x, y, 3, 500)
            pop()


def grid(x, y, order, spacing, function, *args):
    with pushMatrix():
        translate(x - order * spacing / 2, y- order * spacing / 2)
        for i in range(order):
            gx = spacing/2 + i * spacing 
            for j in range(order):
                gy = spacing/2 + j * spacing
                function(gx, gy, *args) 
    
def keyPressed():
    if key == " ": random_seed(renew=True)
    if key == "s": saveFrame("###.png")
    
def random_seed(renew=False):
    global rnd_seed
    if renew:
        rnd_seed = randint(0, 1000)
    else:
        #from random import seed
        seed(rnd_seed)
        randomSeed(rnd_seed)
        
        
def face(xo, yo, n, tw, e=None):
    cw = tw / n
    offset = (cw - tw) / 2.
    for i in range(n):
        x = xo + offset + cw * i
        for j in range(n):
            y = yo + offset + cw * j
            o = (i + j) % 10
            if e is not None:
                element(x, y, cw, e)
            elif cw > 20 and random(10) < 5:
                face(x, y, 3, cw)
            elif cw > 30:
                face(x, y, 3, cw, o)


def element(x, y, w, option):
    # fill(0)
    if option == 0:
        t = choice(('a', 'b', 'c'))
        textSize(w/3)
        text(t, x, y)
    else:
        t = choice(('1A', '2B', '3C'))
        textSize(w / 3)
        text(t, x, y)
