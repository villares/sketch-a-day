
import py5
import shapely

pts = [
    (100, 100), (300, 150), (200, 400), (100, 300)
    ]
D = 50 + 12.5
HD = 50 - 12.5
altura = 50

def setup():
    py5.size(512, 512)
    py5.no_stroke()

def draw():
    py5.background(0)    
#     largura = R * 1.5
#     altura = R * py5.sqrt(3)

    largura = altura / py5.sqrt(3) * 1.5
    num = int(py5.width / largura)
    py5.fill(255, 200)
    poly = shapely.Polygon(pts)
    for fila in range(num):
        for coluna in range(num):  # 0, 1, ... 9
            x = int(coluna * largura)
            if coluna % 2 == 1:  # colunas impares
                y = fila * altura
            else:                # colunas pares
                y = fila * altura + altura / 2
            hole = shapely.Point(x, y).buffer(HD/2)
            ring = shapely.Point(x, y).buffer(D/2) - hole 
            if poly.intersects(ring):
                py5.shape(ring)    
                #poligono(x, y, R)
    py5.fill(0, 100, 200)
    for x, y in pts:
        py5.circle(x, y, 5)
                
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
