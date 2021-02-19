
add_library('geomerative')

linhas = []
DIST_PONTOS = 4  # na conversão da fonte em polígonos
RAIO = 100
texto = "ABC123"
tamanho = 100
x = 10
y = 120

def setup():
    size(400, 400)
    noStroke()
    RG.init(this)
    RG.setPolygonizer(RG.UNIFORMLENGTH)
    RG.setPolygonizerLength(DIST_PONTOS)
    s = 40
    glifos = [RG.getText(letra, "Tomorrow-Bold.ttf", s, LEFT) for letra in texto]
    
    global point_groups
    point_groups = []
    for g in glifos:
            point_groups.append(g.getPointsInPaths())
    calcTam(point_groups)

def draw():

    background(255)
    for pg in point_groups:
        fill(0)
        noStroke()
        for glifo in pg:
            if glifo:
                beginShape()
                # path dentro de cada Linha
                for i_contorno, contorno in enumerate(glifo):
                    if i_contorno > 0:
                        beginContour()  # se a Linha tiver olho
                    # pontos de cada path
                    for vertice in contorno:
                        y = vertice.y + sy
                        x = vertice.x + sx
                        vertex(x, y)
                    if i_contorno > 0:
                        endContour()
                endShape(CLOSE)


def calcTam(glifos):
        tamLetras = [PVector()] * len(glifos)
        wTotal = 0
        hTotal = 0
        for i, glifo in enumerate(glifos):  # Linha
            wLetra = 0
            hLetra = 0
            if glifo:
                # path dentro de cada Linha
                for contorno in glifo:
                    # pontos de cada path
                    for vertice in contorno:
                        x = vertice.x
                        y = vertice.y
                        if x > wLetra:
                            wLetra = x
                        if y > hLetra:
                            hLetra = y
                        x += wTotal
                        vertice.x += wTotal
            else:
                wLetra +=  tamLetras[i - 1].x
            tamLetras[i] = PVector(wLetra, hLetra)
            if hLetra > hTotal:
                hTotal = hLetra
            wTotal += wLetra
