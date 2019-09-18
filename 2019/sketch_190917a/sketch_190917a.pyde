"""
Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day

Box with round holes
"""

add_library('GifAnimation')
from gif_exporter import gif_export
from parts import Face
from glue_tab import glue_tab

faces = []
THICK = 20

def setup():
    size(500, 500, P3D)
    hint(ENABLE_DEPTH_SORT)


def draw():
    background(200, 210, 220)
 
    # Face
    fill(255, 100)
    face_2D(250, 100, 250, 150, 15)
    # Caixa
    translate(250, 300)
    rotateX(QUARTER_PI + frameCount/50.)
    caixa(250, 150, 100, 15)    

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
    
    
def caixa(w, h, d, e=0):
     mw, mh, md = w/2., h/2., d/2.
     translate(0, 0, -md) # base
     face_2D(0, 0, w, h, e)
     translate(0, 0, d) # topo
     face_2D(0, 0, w, h, e)
     translate(0, 0, -md) # volta
     rotateY(HALF_PI)
     translate(0, 0, -mw) # lateral e
     face_2D(0, 0, d, h, e)
     translate(0, 0, w) # lateral d
     face_2D(0, 0, d, h, e)
     translate(0, 0, -mw) # volta    
     rotateY(-HALF_PI)  # volta
     rotateX(HALF_PI)
     translate(0, 0, -mh) # lateral e
     face_2D(0, 0, w, d, e)
     translate(0, 0, h) # lateral d
     face_2D(0, 0, w, d, e)
     translate(0, 0, -mw) # volta         
     rotateX(-HALF_PI)

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
