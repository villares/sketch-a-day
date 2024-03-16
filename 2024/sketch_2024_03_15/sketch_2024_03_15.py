from trimesh.creation import extrude_polygon
from shapely import Point

R = 250  # Raio do anel (eixo)
E = 100  # Espessura do anel (alter furo central)
F = 40   # Raio dos furos
N = 12   # número de furos
A = 20   # Altura do anel (em Z)

def setup():
    size(600, 600, P3D)
    xc, yc = width / 2, height / 2
    ca = shp_circle(xc, yc, R + E / 2)    
    cb = shp_circle(xc, yc, R - E / 2)    
    anel = ca.difference(cb)
    angulo = radians(360) / N
    for n in range(N):
        a = angulo * n
        x = xc + R * cos(a)
        y = yc + R * sin(a)
        f = shp_circle(x, y, F)        
        anel = anel.difference(f)
     
    global resultado, shp
    resultado = extrude_polygon(anel, A)
    shp = convert_shape(resultado)
    shp.disable_style()

def draw():
    lights()
    no_stroke()
    translate(0, 0, -140)
    rotate_x(radians(30))
    shape(shp, 0, 0)
 
def shp_circle(x, y, r):
    return Point((x, y)).buffer(r)

def key_pressed():
    resultado.export('out.stl')
    save(__file__[:-2] + 'png')

    