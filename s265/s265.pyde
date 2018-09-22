# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
SKETCH_NAME = "s265"  # 20180920
OUTPUT = ".png"

def setup():
    size(660, 660)
    noFill()
    rectMode(CENTER)
    
def draw():
    noLoop()
    background(250) 
    grid(width/2, height/2, 5, 130, ensamble, 5) # ensamble of 5 , on grid also order=5

def ensamble(ex, ey, order):
    with pushMatrix():
        translate(ex, ey)
        for _ in range(order): 
            order, spacing, side, radius = int(random(3, 9)), 10, 5, random(-3, 3)
            x, y = random(-25, 25), random(-25, 25)    
            grid(x, y, order, spacing, rect, side, side, *[radius]*4)

def grid(x, y, order, spacing, function, *args):
    with pushMatrix():
        translate(x - order * spacing / 2, y- order * spacing / 2)
        for i in range(order):
            for j in range(order):
                    function(spacing/2 + i * spacing, spacing/2 + j * spacing, *args) 
    
def keyPressed():
    if key == " ": loop()
    
# print text to add to the project's README.md             
def settings():
    println(
"""
![{0}]({0}/{0}{2})
{1}: [code](https://github.com/villares/sketch-a-day/tree/master/{0}) [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]
""".format(SKETCH_NAME, SKETCH_NAME[1:], OUTPUT)
    )
