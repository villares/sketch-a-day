"""
Baseado em exemplo de André Burnier portado do Processing Java para Python
por Thiago Bellotti e Alexandre Villares (https://abav.lugaralgum.com)
Brincando com vértices da fonte Tomorrow de Tony de Marco e Monica Rizzolli
"""

add_library('geomerative')

linhas = []
DIST_PONTOS = 4  # na conversão da fonte em polígonos
RAIO = 100
texto = "Python/Process/ing+geo/merative"
tamanho = 100
x = 10
y = 120

def setup():
    size(400, 400)
    noStroke()
    RG.init(this)
    tx = texto.split("/")
    y_offset = 0
    for linha in tx:
        linhas.append(Linha(tamanho, linha, y_offset))
        y_offset += tamanho * 0.8

def draw():

    background(255)
    for linha in linhas:
        fill(0)
        noStroke()
        linha.desenhaFormas(x, y)

        # Se quiser mostrar os pontos originais das letras
        # for v in linha.vertices_base:
        #     fill(255)
        #     stroke(0)
        #     ellipse(x + v.x, y + v.y + linha.ly, 5, 5)

        for v in linha.vertices_visiveis:
            fill(255)
            stroke(0)
            # ajusta para x, y e 'y da linha'
            vx, vy = x + v.x, y + v.y + linha.ly
            if mousePressed and mouse_over(vx, vy, 100, 100):
                fill(255, 0, 0)
                ellipse(vx, vy, 5, 5)
                v.x += (mouseX - pmouseX)
                v.y += (mouseY - pmouseY)
        # fazendo os vertices voltarem para casa (base)
        linha.voltaVertices()

def mouse_over(x, y, w, h):
    return (x - w / 2 < mouseX < x + w / 2 and
            y - h / 2 < mouseY < y + h / 2)

class Linha:

    def __init__(self, tam, texto, y):
        self.ly = y
        letras = []
        for l in texto:
            letras.append(RG.getText(l, "Tomorrow_Light.ttf", tam, LEFT))

        RG.setPolygonizer(RG.UNIFORMLENGTH)
        RG.setPolygonizerLength(DIST_PONTOS)

        self.points = []
        self.base_points = []
        for l in letras:
            self.points.append(l.getPointsInPaths())
            self.base_points.append(l.getPointsInPaths())

        # ajusta a posição das letras
        self.tamLetras = [PVector()] * len(texto)
        self.calcTam(self.points)
        self.calcTam(self.base_points)

        # produz lista 'planas' dos pontos
        self.vertices_visiveis = self.listaVertices(self.points)
        self.vertices_base = self.listaVertices(self.base_points)

    def desenhaFormas(self, sx, sy):
        glifos = self.points
        # for i in range(len(pontos)):  # Linha
        for glifo in glifos:
            if glifo:
                beginShape()
                # path dentro de cada Linha
                for i_contorno, contorno in enumerate(glifo):
                    if i_contorno > 0:
                        beginContour()  # se a Linha tiver olho
                    # pontos de cada path
                    for vertice in contorno:
                        y = vertice.y + sy + self.ly
                        x = vertice.x + sx
                        vertex(x, y)
                    if i_contorno > 0:
                        endContour()
                endShape(CLOSE)

    def calcTam(self, glifos):
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
                wLetra += self.tamLetras[i - 1].x
            self.tamLetras[i] = PVector(wLetra, hLetra)
            if hLetra > hTotal:
                hTotal = hLetra
            wTotal += wLetra

    def listaVertices(self, glifos):
        vertices = []
        for glifo in glifos:
            if glifo:
                # path dentro de cada Linha
                for contorno in glifo:
                    # pontos de cada path
                    for vertice in contorno:
                        vertices.append(vertice)
        return vertices

    def voltaVertices(self):
        for base, moved in zip(self.vertices_base, self.vertices_visiveis):
            if dist(base.x, base.y, moved.x, moved.y) > 0:
                moved.x += (base.x - moved.x) / 30
                moved.y += (base.y - moved.y) / 30
