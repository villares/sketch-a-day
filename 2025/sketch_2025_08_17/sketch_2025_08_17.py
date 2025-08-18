
import py5
import shapely

pts = [
    (100, 100), (300, 150), (200, 400), (100, 300)
    ]

def setup():
    py5.size(512, 512)

def draw():
    py5.background(0)    
    R = 10
    largura = R * 1.5
    altura = R * py5.sqrt(3)
    num = int(py5.width / largura)
    
    for fila in range(num):
        for coluna in range(num):  # 0, 1, ... 9
            x = int(coluna * largura)
            if coluna % 2 == 1:  # colunas impares
                y = fila * altura
            else:                # colunas pares
                y = fila * altura + altura / 2
            if shapely.Polygon(pts).contains(shapely.Point(x, y)):
                py5.circle(x, y, altura)    
                #poligono(x, y, R)

def key_pressed():
    py5.save_frame('out.png')

def poligono(xc, yc, ra, pontos=6):
    ang = py5.TWO_PI / pontos
    with py5.begin_closed_shape():
        py5.vertices(
            (xc + py5.cos(ang * i) * ra,
             yc + py5.sin(ang * i) * ra)
             for i in range(pontos)
        )

py5.run_sketch(block=False) 
