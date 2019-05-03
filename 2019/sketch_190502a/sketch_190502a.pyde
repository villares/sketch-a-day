"""
Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day

- Unfolding piramids
"""

# add_library('GifAnimation')
# from gif_exporter import gif_export

CORTE = color(255, 0, 0)
DOBRA = color(0, 0, 255)

raio_externo, raio_interno = 100, 50
lados = 5

def setup():
    size(400, 600, P3D)
    hint(ENABLE_DEPTH_TEST)
    hint(ENABLE_DEPTH_SORT)

def draw():
    background(240)
    translate(width / 2, height / 4 + 50)
    pushMatrix()
    rotateX(radians(45))
    rotateZ(radians(frameCount / 3.))
    fill(255, 200)
    stroke(0)
    strokeWeight(2)
    pontos = piramide_3D(lados, raio_externo, raio_interno)
    popMatrix()
    translate(0, height / 2 - 50)
    piramide_desdobrada(pontos)

def piramide_3D(np, re, ri):
    # calculando os pontos
    pontos = []
    n = np * 2
    for i in range(n):
        ang = radians(i * 360. / n)
        if i % 2 == 0:
            r = ri
        else:
            r = re
        x = sin(ang) * r
        y = cos(ang) * r
        pontos.append((x, y))
    # arestas da base
    pontos_base = pontos[::2]
    pontos_base2 = pontos_base[1:] + [pontos_base[0]]
    arestas_base = zip(pontos_base, pontos_base2)
    # calculo da altura
    (p0x, p0y), (p1x, p1y) = pontos[0], pontos[1]
    lado = dist(p0x, p0y, p1x, p1y)
    h_squared = lado * lado - ri * ri
    if h_squared > 0:  # se a altura viavel
        h = sqrt(h_squared)
        for aresta in arestas_base:
            p1, p2 = aresta
            beginShape()
            vertex(*p1)
            vertex(*p2)
            vertex(0, 0, h)
            endShape(CLOSE)
    # sempre desenha a base
    beginShape()
    for ponto in pontos_base:
        vertex(*ponto)
    endShape(CLOSE)
    # devolve os pontos para usar no 2D!
    return pontos

def piramide_desdobrada(pontos):
    noFill()
    # dobras da base
    stroke(DOBRA)
    beginShape()
    for ponto in pontos[::2]:
        vertex(*ponto)
    endShape(CLOSE)
    # arestas laterais
    lista_b = pontos[1:] + [pontos[0]]
    arestas = zip(pontos, lista_b)
    for i, aresta in enumerate(arestas):
        p1, p2 = aresta
        stroke(CORTE)
        if i % 2 == 0:
        # abas de cola
            glue_tab(p2, p1, 10, )
            # dobra
            stroke(DOBRA)
            line(p2[0], p2[1], p1[0], p1[1])
        else:
            # outra aresta cortada
            line(p1[0], p1[1], p2[0], p2[1])

def glue_tab(p1, p2, tab_w, cut_ang=QUARTER_PI / 3):
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

    if edge_len > 2 * cut_len * cos(cut_ang):    # 'normal' trapezoidal tab
        beginShape()
        vertex(*p1)    # vertex(p1[0], p1[1])
        vertex(*f1)
        vertex(*f2)
        vertex(*p2)
        endShape()
    else:    # short triangular tab
        fm = ((f1[0] + f2[0]) / 2, (f1[1] + f2[1]) / 2)
        beginShape()
        vertex(*p1)
        vertex(*fm)    # middle way of f1 and f2
        vertex(*p2)
        endShape()

def keyPressed():
    global raio_interno, raio_externo, lados
    if keyCode == UP:
        raio_externo += 5
    if keyCode == DOWN:
        raio_externo -= 5
    if keyCode == LEFT:
        raio_interno += 5
    if keyCode == RIGHT:
        raio_interno -= 5
    if key == "+":
        lados += 1
    if key == "-" and lados > 3:
        lados -= 1

    # if key == "g":
    #     gif_export(GifMaker, filename=SKETCH_NAME)

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
