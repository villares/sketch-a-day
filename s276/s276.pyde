# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
SKETCH_NAME = "s276"  # 20181001
OUTPUT = ".png"

from random import choice
from random import randint

#ascii = """ .`:,';-_*"~!i|/\rI^)+(l?{><=}tc[]sjvJL7f1xzTyYF5e23onuaV4$SkC#EPhZX96U0pqKdbGA%gH8wRBmODN&Q@WM"""
ascii = """ .`:,';-_*"~!i|/\rI^)+(l?{><=}[]7f1xzT5234SC#EZX96U0%gH8RABODN&@WM"""


def setup():
    size(1200, 600)
    rectMode(CENTER)
    colorMode(HSB)
    #fill(0, 200)
    f = createFont("SourceCodePro-Bold", 14)
    textFont(f)
    textSize(14)
    global mi, ma
    mi, ma = 3, 15
    
def draw():
    noLoop()
    background(200) 
    grid(width/4, height/2, 4, 150, ensamble, 5) # ensamble of 5 , on grid also order=5
    grid(width/4*3, height/2, 4, 150, ensamble, 5) # ensamble of 5 , on grid also order=5


def ensamble(ex, ey, order):
    with pushMatrix():
        translate(ex, ey)
        rotate(QUARTER_PI)
        gliph = lambda x, y, l: text(l, x, y)
        for _ in range(order): 
            rotate(HALF_PI)
            c = choice(ascii)
            order, spacing, side = randint(mi, ma), 14, 7
            x, y = int(random(-5, 5)) * side, int(random(-5, 5)) * side 
            fill(randint(1 , 5) * 48, 255, 255) # H, S, B
            grid(x, y, order, spacing, gliph, c)


def grid(x, y, order, spacing, function, *args):
    with pushMatrix():
        translate(x - order * spacing / 2, y- order * spacing / 2)
        for i in range(order):
            gx = spacing/2 + i * spacing 
            for j in range(order):
                gy = spacing/2 + j * spacing
                function(gx, gy, *args) 
    
def keyPressed():
    if key == " ": loop()
    if key == "s": saveFrame("###.png")
    
# print text to add to the project's README.md             
def settings():
    println(
"""
![{0}]({0}/{0}{2})
{1}: [code](https://github.com/villares/sketch-a-day/tree/master/{0}) [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]
""".format(SKETCH_NAME, SKETCH_NAME[1:], OUTPUT)
    )
