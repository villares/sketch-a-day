from random import choice

def setup():
    size(700, 700)
    rectMode(CENTER)
    strokeJoin(ROUND)
    noLoop()

def draw():
    background(0)
    g = list(grid(700, 20, 700, 20))
    # println(g)
    for _ in range(20):
        x, y = choice(g)
        fill(x / 3, y / 3, 255, 100)
        circle(x, y, 10)
        poly_arrow(width / 2, width / 2, x, y)

def grid(w, cols, h, rows):
    cw = w / cols
    rh = h / rows
    for x in range(cw / 2, w, cw):
        for y in range(rh / 2, h , rh):
            yield x, y

def poly_arrow(x, y, w, h):
    """ Seta na posição x, y com largura w e altura h"""
    mw = w / 2
    mh = h / 2
    pushMatrix()  # preserva o sistema de coordenadas atual
    translate(x, y)  # translada a origem do sistema de coordenadas
    r = choice((0, 1, 2, 4))
    rotate(r * HALF_PI)
    beginShape()  # começa a desenhar a forma, inicia um polígono
    vertex(0, -0 - mw)
    vertex(-mw  , 0)
    vertex(-mw, mh)
    vertex(0, mh - mw)
    vertex(mw, mh)
    vertex(mw, 0)
    # vertex(0, 0)
    endShape(CLOSE)  # encerra a forma a fechando no primeiro vértice
    popMatrix() # retorna o sistema de coordenadas anterior
    

def keyPressed():
    if key == 's':
        saveFrame("####.png")
    redraw()
    
    
 
# print text to add to the project's README.md
def settings():
    from os import path
    global SKETCH_NAME
    SKETCH_NAME = path.basename(sketchPath())
    OUTPUT = ".png"
    println(
        """
![{0}](2019/{0}/{0}{1})
[{0}](https://github.com/villares/sketch-a-day/tree/master/2019/{0}) [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]
""".format(SKETCH_NAME, OUTPUT)
    )
