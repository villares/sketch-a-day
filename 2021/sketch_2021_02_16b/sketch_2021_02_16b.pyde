
from villares.line_geometry import draw_poly, rotate_point
from villares.arcs import arc_filleted_poly, arc_augmented_poly
from random import choice

cores = (0, 64, 128)
f = 0 

def setup():
    size(600, 600)
    strokeWeight(5)
    noFill()
    colorMode(HSB)
    blendMode(ADD)
    global lista_formas, lista_proximos
    lista_formas = cria_formas()
    lista_proximos = cria_formas()
    
    
def cria_formas(n=2):
    lista_formas = []
    while len(lista_formas) < n:
        cor = choice(cores)
        x = choice(range(200, width - 200, 25))
        y = choice(range(200, width - 200, 25))
        w = choice((-300, -200, 200, 300))
        h = choice((250, 200, 150, 100))
        ang = choice((0, 0, TWO_PI, HALF_PI, -HALF_PI))
        px, py = forma(x, y, w, h, angle=ang)[4]
        forma_bom = True
        for b in lista_formas:
            pobx, poby = b[-2], b[-1]
            if dist(pobx, poby, px, py) < 50:
                forma_bom = False
        if forma_bom:
            lista_formas.append((cor, x, y, w, h, ang, px, py))    
    return lista_formas

def draw():
    global lista_formas, lista_proximos
    global f
    background(0)
    # t = map(mouseX, 0, width, 0, 1)
    # t = 1
    # for f in range (0, 361, 30):
  
    t = 1 - abs(sin(radians(f)))

    for i, (a, b) in enumerate(zip(lista_formas, lista_proximos))  :
        # lista_formas[i] = lerp_forma(a, b, float(mouseX) / width)
        cor, x, y, w, h, ang, px, py = lerp_forma(a, b, t)
        # cor, x, y, w, h, ang = lerp_forma(a, b, map(mouseX, 0, width, 0, 1))
        stroke(cor)
        for j in range(4):
            stroke((cor + j * 64) % 255, 200, 200)
            pts = forma(x, y,
                        # x  * (1 - 0.00 * j), y  * (1 - 0.00 * j),
                        w * (1 - 0.20 * t * j),
                        h * (1 - 0.20 * t * j), angle=ang)
            arc_augmented_poly(pts, [-25 + 50 * t * j] * len(pts))
            # arc_filleted_poly(pts, [100] * len(pts))

    if f % 180 == 0: 
        lista_formas = cria_formas()
    f += 0.5
    # print(f, t)


def lerp_forma(a, b, t):
    cor = [lerpColor(a[0], b[0], t)]
    other = [lerp(aa, bb, t) for aa, bb in zip(a[1:], b[1:])]
    return tuple(cor + other)
            
def forma(ox, oy, w, h, ponta=None, mode=CENTER, angle=None):
    wbase = w / 4
    offset = 0
    if mode == CENTER:
        x, y = ox - w / 2.0, oy - h / 2.0
    else:
        x, y = ox, oy
    px, py = ponta or x + w / 2.0, y #+ h * 0.5
    
    points = [(x, y), (x + w, y),
              (x + w, y + h),
              (offset + x + w / 2 + wbase / 2, y + h),
              (px, py),  # (x + w / 2, y + h),
              (offset + x + w / 2 - wbase / 2, y + h),
              (x, y + h)]
    if angle is None:
        return points
    else:
        return [rotate_point((x, y), angle, (ox, oy))
                for x, y in points]
        
def keyPressed():
    if key == ' ':
        global lista_formas, lista_proximos
        lista_formas = cria_formas()
