# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
SKETCH_NAME = "s264"  # 20180919
OUTPUT = ".png"

def setup():
    size(600, 600)
    noFill()
    rectMode(CENTER)
    
def draw():
    noLoop()
    background(255)
    for _ in range(100): 
        order = int(random(5, 10))
        spacing = 20 
        radius = random(0, 5)
        x = random(order * spacing/2, width - order * spacing/2)
        y = random(order * spacing/2, height - order * spacing/2)            
        grid(x, y, order, spacing,
            rect, 10, 10, *[radius]*4)

def grid(x, y, order, spacing, function, *args):
    with pushMatrix():
        translate(x - order * spacing / 2, y- order * spacing / 2)
        for i in range(order):
            for j in range(order):
                    function(spacing/2 + i * spacing, spacing/2 + j * spacing,
                             *args) 
    
def keyPressed():
    if key == " ": loop()

     
# def squares(order, i, j, x, y, spacing, w):
#     with pushMatrix():
#         translate(x - order * spacing / 2, y- order * spacing / 2)
#         rect(spacing/2 + i * spacing, spacing/2 + j * spacing, w, w) 

# def grid(x, y, order, spacing, function, *args):
#     for i in range(order):
#             for j in range(order):
#                     function(order, i, j, *args) 

# print text to add to the project's README.md             
def settings():
    println(
"""
![{0}]({0}/{0}{2})
{1}: [code](https://github.com/villares/sketch-a-day/tree/master/{0}) [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]
""".format(SKETCH_NAME, SKETCH_NAME[1:], OUTPUT)
    )
