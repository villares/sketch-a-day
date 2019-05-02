# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
# unfolded piramid

def setup():
    size(600, 600)
    
def draw():
    background(200)
    translate(300, 300)
    pontos = estrela(4, 200, 75)
    fill(255)
    beginShape()
    for i, ponto in enumerate(pontos):
        vertex(*ponto)
    endShape(CLOSE)
    noFill()
    beginShape()
    for i, ponto in enumerate(pontos):
        if i % 2 == 0:
            #text(str(i//2), ponto[0], ponto[1])
            vertex(*ponto)
    endShape(CLOSE)    
    lista_b = pontos[1:] + [pontos[0]]
    arestas = zip(pontos, lista_b)
    abas = arestas[::2]
    fill(255)
    for a in abas:
        p1, p2 = a
        glue_tab(p2, p1, 10)
    
def estrela(np, re, ri):
    vertices_estrela = []
    n = np * 2
    for i in range(n):
        ang = radians(i * 360. / n)
        if i % 2 == 0: r = ri
        else: r = re
        x = sin(ang) * r
        y = cos(ang) * r
        vertices_estrela.append((x, y))
    return vertices_estrela

def glue_tab(p1, p2, tab_w, cut_ang=QUARTER_PI):
    """
    draws a trapezoidal or triangular glue tab along edge defined by p1 and p2,
    with width tab_w and cut angle a
    """
    al = atan2(p1[0] - p2[0], p1[1] - p2[1])
    a1 = al + cut_ang + PI
    a2 = al - cut_ang
    # calculate cut_len to get the right tab width
    cut_len = tab_w / sin(cut_ang)
    f1 = (p1[0] + cut_len * sin(a1),
          p1[1] + cut_len * cos(a1))
    f2 = (p2[0] + cut_len * sin(a2),
          p2[1] + cut_len * cos(a2))
    edge_len = dist(p1[0], p1[1], p2[0], p2[1])

    if edge_len > 2 * cut_len * cos(cut_ang):  # 'normal' trapezoidal tab
        beginShape()
        vertex(*p1)  # vertex(p1[0], p1[1])
        vertex(*f1)
        vertex(*f2)
        vertex(*p2)
        endShape()
    else:  # short triangular tab
        fm = ((f1[0] + f2[0]) / 2, (f1[1] + f2[1]) / 2)
        beginShape()
        vertex(*p1)
        vertex(*fm)  # middle way of f1 and f2
        vertex(*p2)
        endShape()    


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
