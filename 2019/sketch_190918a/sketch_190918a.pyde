"""
Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day

Box with round holes
"""

add_library('GifAnimation')
from gif_exporter import gif_export
from frame_box import frame_box, unfolded_frame_box

faces = []
THICK = 20
modes = [-1, 0, 1]  # click mouse to switch modes

def setup():
    size(600, 600, P3D)
    hint(ENABLE_DEPTH_SORT)

def draw():
    background(200, 210, 220)
    translate(300, 300)
    w, h, d, thick = (250, 150, 100, 30)
    if modes[0] >= 0:
        fill(255, 100)
        stroke(0)
        pushMatrix()
        translate(0, 0, 200)
        rotateX(QUARTER_PI + frameCount/50.)
        frame_box(w, h, d, thick)
        popMatrix()
    if modes[0] <= 0:
        unfolded_frame_box(w, h, d, thick)

    if frameCount/50. < TWO_PI:
        if frameCount % 2:
            gif_export(GifMaker, filename=SKETCH_NAME)
    else:
        exit()

    
def face_2D(x, y, w, h, e=0, closed=True):
    mw, mh = w/2., h/2.
    pushMatrix()
    translate(x, y)
    beginShape()
    vertex(-mw, -mh)
    vertex(+mw, -mh)
    vertex(+mw, +mh)
    vertex(-mw, +mh)
    if e > 0 and mw - e > 0 and mh - e > 0:
            beginContour()
            np = 24
            for i in range(np):
                ang = TWO_PI / np * i
                x = sin(ang) * e
                y = cos(ang) * e
                vertex(x, y)
            endContour()
    if closed:
        endShape(CLOSE)
    else:
        endShape()
    popMatrix()

def mousePressed():
    modes[:] = modes[1:] + [modes[0]]

# print text to add to the project's README.md
def settings():
    from os import path
    global SKETCH_NAME
    SKETCH_NAME = path.basename(sketchPath())
    OUTPUT = ".gif"
    println(
        """
![{0}](2019/{0}/{0}{1})

[{0}](https://github.com/villares/sketch-a-day/tree/master/2019/{0}) [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]
""".format(SKETCH_NAME, OUTPUT)
    )
