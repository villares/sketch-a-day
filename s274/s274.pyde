# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
SKETCH_NAME = "s274"  # 20180929
OUTPUT = ".png"

from random import choice
letter = " "
ascii = """ .`:,';-_*"~!i|/\rI^)+(l?{><=}tc[]sjvJL7f1xzTyYF5e23onuaV4$SkC#EPhZX96U0pqKdbGA%gH8wRBmODN&Q@WM"""
gliphs = [ # lambda x, y, s: rect(x, y, s, s),
           # lambda x, y, s: ellipse(x, y, s, s),
           # lambda x, y, s: triangle(x - s, y, x - s, y + s, x, y + s),
           # lambda x, y, s: triangle(x + s, y, x + s, y - s, x, y - s),
           lambda x, y, s: text(letter, x, y)
           ]

def setup():
    size(1200, 600)
    rectMode(CENTER)
    colorMode(HSB)
    stroke(0)
    f = createFont("SourceCodePro-Bold", 14)
    textFont(f)
    # textSize(14)

    
def draw():
    noLoop()
    background(200) 
    grid(width/4, height/2, 4, 150, ensamble, 5) # ensamble of 5 , on grid also order=5
    grid(width/4*3, height/2, 4, 150, ensamble, 5) # ensamble of 5 , on grid also order=5

def ensamble(ex, ey, order):
    with pushMatrix():
        translate(ex, ey)
        for _ in xrange(order): 
            #fill(int(random(5)) * 32, 255, 250, 255) #fill(random(4) * 64, 255, 255, 100)
            global letter
            letter = choice(ascii)
            fill(0)
            noFill()
            order, spacing, side = int(random(3, 6)), 14, 7
            x, y = int(random(-5, 5)) * side, int(random(-5, 5)) * side    
            grid(x, y, order, spacing, choice(gliphs), side)

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
