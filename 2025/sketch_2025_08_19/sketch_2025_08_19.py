
import py5
import shapely
import trimesh

pts = [
    (100, 100), (300, 150),
    (400, 300), (100, 450)
    ]
CD = 50 + 12.5
HD = 50 - 12.5
altura = 50
D = 10
shapes = []

def setup():
    py5.size(512 + 256, 512, py5.P3D)
    py5.no_stroke()
    calc_shapes()

def draw():
    py5.background(0)
    py5.lights()
    py5.fill(255, 200)
    #py5.shape(shapely.unary_union(shapes))
    py5.shape(poly)
    py5.fill(0, 100, 200)
    for x, y in pts:
        py5.circle(x, y, 5)
    py5.translate(256, 0)
    py5.fill(255)
    py5.rotate_x(py5.radians(30))
    py5.shape(mesh)
                


def calc_shapes():
    global poly, mesh
    largura = altura / py5.sqrt(3) * 1.5
    num = int(py5.width / largura)
    poly = shapely.Polygon(pts)
    for fila in range(num):
        for coluna in range(num):  # 0, 1, ... 9
            x = int(coluna * largura)
            if coluna % 2 == 1:  # colunas impares
                y = fila * altura
            else:                # colunas pares
                y = fila * altura + altura / 2
            hole = shapely.Point(x, y).buffer(HD/2)
            ring = shapely.Point(x, y).buffer(CD/2) - hole 
            if poly.contains(ring):
                shapes.append(ring)
    poly = shapely.unary_union(shapes)
    mesh = trimesh.creation.extrude_polygon(poly, D)

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
