# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day

from frame_box import frame_box, unfolded_box

modes = [-1, 0, 1] # click mouse to switch modes

def setup():
    size(600, 600, P3D)

def draw():
    background(200)
    translate(300, 300)
    if modes[0] >= 0:
        fill(255)
        stroke(0)
        pushMatrix()
        translate(0, 0, 200)
        rotateX(HALF_PI / 2)
        frame_box(250, 150, 100, 30)
        popMatrix()
    if modes[0] <= 0:
        unfolded_box(250, 150, 100, 30)

def mousePressed():
    modes[:] = modes[1:] + [modes[0]]
    
def keyPressed():
    saveFrame("a###.png")
    
# para gerar o markdown que vai na página do sketch-a-day    
def settings():
    from os import path
    global SKETCH_NAME
    SKETCH_NAME = path.basename(sketchPath())
    OUTPUT = ".gif"
    println(
        """
![{0}]({2}/{0}/{0}{1})

[{0}](https://github.com/villares/sketch-a-day/tree/master/{2}/{0}) [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]
""".format(SKETCH_NAME, OUTPUT, year())
    )
