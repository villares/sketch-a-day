# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
SKETCH_NAME = "s264"  # 20180919
OUTPUT = ".png"

def setup():
    size(600, 600)
    noFill()
    rectMode(CENTER)
    strokeWeight(3)

    
def draw():
    background(255)
    translate(width/2, height/2)
    grid(20, squares, 20, 10)
    
def squares(i, j, spacing, w):
    with pushMatrix():
        translate(-order * spacing / 2, -order * spacing / 2)
        rect(spacing/2 + i * spacing, spacing/2 + j * spacing, w, w) 

def grid(order, function, *args):
    for i in range(order):
            for j in range(order):
                    function(i, j, , order, *args) 

# print text to add to the project's README.md             
def settings():
    println(
"""
![{0}]({0}/{0}{2})
{1}: [code](https://github.com/villares/sketch-a-day/tree/master/{0}) [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]
""".format(SKETCH_NAME, SKETCH_NAME[1:], OUTPUT)
    )
