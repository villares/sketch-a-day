import py5
import shapely
import trimesh

pts = [
    (100, 100), (200, 125), (300, 150), 
    (400, 300), (100, 450)
    ]
CD = 50 + 12.5
HD = 50 - 12.5
altura = 50
D = 30
shapes = []
drag = None

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
        if py5.dist(py5.mouse_x, py5.mouse_y, x, y):
            py5.fill(0, 255, 0)
        else:
            py5.fill(0, 100, 200)    
        py5.circle(x, y, 10)
    py5.translate(256, 0)
    py5.fill(255)
    py5.rotate_x(py5.radians(30))
    py5.shape(mesh)
                
def calc_shapes():
    global poly, mesh
    shapes.clear()
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
    global altura, CD, HD
    if py5.key == 'p':
        py5.save_frame('out.png')
    elif py5.key == 'q':
        CD += 1
    elif py5.key == 'a':
        CD -= 1
    elif py5.key == 'w':
        HD += 1
    elif py5.key == 's':
        HD -= 1
    elif py5.key == 'e':
        altura += 1
    elif py5.key == 'd':
        altura -= 1
    calc_shapes()
    
def mouse_pressed():
    global drag
    for i in range(len(pts)):
        if py5.dist(*pts[i], py5.mouse_x, py5.mouse_y) < 10:
            drag = i
            break
        
def mouse_dragged():
    if drag is not None:
        pts[drag] = py5.mouse_x, py5.mouse_y

def mouse_released():
    global drag
    if drag is not None:
        calc_shapes()
        drag = None
    
py5.run_sketch(block=False)