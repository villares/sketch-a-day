# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
SKETCH_NAME = "s279"  # 20181004
OUTPUT = ".gif"

add_library('peasycam')
from random import seed
from random import choice
from random import randint

ascii = """ .`:,';-_*"~!i|/\rI^)+(l?{><=}tc[]sjvJL7f1xzTyYF5e23onuaV4$SkC#EPhZX96U0pqKdbGA%gH8wRBmODN&Q@WM"""
#ascii = """ .`:'-_*"~|/\^)+{><=}[]#"""
rnd_seed = 1000

def setup():
    size(600, 600, P3D)
    smooth()
    rectMode(CENTER)
    colorMode(HSB)
    fill(0)
    
    cam = PeasyCam(this, 400)
    f = createFont("SourceCodePro-Bold", 64)
    textFont(f)
    textSize(14)
    global mi, ma
    mi, ma = 5, 10

def draw():
    background(100) 
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


def ensamble(ex, ey, order):
        gliph = lambda x, y, l: text(l, x, y)
        for z in range(order): 
            # rotate(QUARTER_PI)
            c = choice(ascii)
            order = randint(mi, ma)
            spacing, side = 14, 14
            x, y = int(random(-5, 5)) * side, int(random(-5, 5)) * side 
            with pushMatrix():
                translate(ex + x, ey + y, z)
                fill(randint(2 , 5) * 32, 255, 255) # H, S, B
                grid(0, 0, order, spacing, gliph, c)


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
    
# print text to add to the project's README.md             
def settings():
    println(
"""
![{0}]({0}/{0}{2})
{1}: [code](https://github.com/villares/sketch-a-day/tree/master/{0}) [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]
""".format(SKETCH_NAME, SKETCH_NAME[1:], OUTPUT)
    )
