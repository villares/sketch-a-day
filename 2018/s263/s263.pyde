# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
SKETCH_NAME = "s263"  # 20180918
OUTPUT = ".png"

def setup():
    size(600, 600)
    noFill()
    rectMode(CENTER)
    strokeWeight(3)

    
def draw():
    background(255)
    grid(x=width/2, y=height/2,
         order=18, spacing=30,
         function=ellipse, w=20)
    grid(x=width/2, y=height/2,
         order=21, spacing=25,
         function=rect, w=20, rule=checker)
    
def every(i, j, order):
    return True            

def checker(i, j, order):
    return (i + j) % 2            

def grid(x, y, order, spacing, function, w, rule=every):
    with pushMatrix():
        translate(x - order * spacing / 2, y - order * spacing / 2)
        for i in range(order):
            for j in range(order):
                if rule(i, j, order):
                    function(spacing/2 + i * spacing, spacing/2 + j * spacing, w, w) 

# print text to add to the project's README.md             
def settings():
    println(
"""
![{0}]({0}/{0}{2})
{1}: [code](https://github.com/villares/sketch-a-day/tree/master/{0}) [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]
""".format(SKETCH_NAME, SKETCH_NAME[1:], OUTPUT)
    )
