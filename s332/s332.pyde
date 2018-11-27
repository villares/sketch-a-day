
# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
SKETCH_NAME = "s332"  # 20181126
OUTPUT = ".png"
NUM = 5
BORDER = 50

from line_geometry import *

#add_library('pdf')
# add_library('gifAnimation')
# from gif_exporter import gif_export

def setup():
    size(500, 500)
    smooth(8)
    init_points(NUM, BORDER)
    background(200)
    print edges(points)
    #beginRecord(PDF, SKETCH_NAME + ".pdf")
    
def draw():
    background(200)
    stroke(0, 100)
    strokeWeight(0.1)
    for pair in edges(points):
        l = Line(*pair)
        l.plot()
    strokeWeight(0.5)
    noFill()
    for p in points:
        ellipse(p.x, p.y, 7, 7)    
    
        
def keyPressed():
    if key == "n" or key == CODED:
        init_points(NUM, BORDER)
        background(200)
        #saveFrame("###.png")
    if key == "s": saveFrame(SKETCH_NAME + ".png")
    if key == "z": 
        for pair in edges(points):
            p = PVector.lerp(pair[0], pair[1], randomGaussian()/4 )
            points.append(p)
            l = Line(*pair)
            l.plot()

def init_points(grid_size, border=0):
    global points
    points = create_points(grid_size, border) 
            
# print text to add to the project's README.md             
def settings():
    println(
"""
![{0}]({0}/{0}{2})

{1}: [code](https://github.com/villares/sketch-a-day/tree/master/{0}) [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]
""".format(SKETCH_NAME, SKETCH_NAME[1:], OUTPUT)
    )
