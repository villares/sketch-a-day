from villares.line_geometry import draw_poly, rotate_point
from random import choice

cores = (color(200, 0, 0), color(255), color(0) )
f = 0 

def setup():
    size(600, 600)
    colorMode(HSB)
    strokeWeight(5)
    noFill()
    global lista_baloes, lista_proximos
    lista_baloes = cria_baloes()
    lista_proximos = cria_baloes()
    
    
def cria_baloes(n=4):
    lista_baloes = []
    for _ in range(n):
        cor = choice(cores)
        x = choice(range(175, width - 175, 25))
        y = choice(range(175, width - 175, 25))
        w = choice((-300, -200, 150, 200, 300))
        h = choice((200, 150, 100, 75))
        a = choice((0, 0, 0, HALF_PI, -HALF_PI))
        lista_baloes.append((cor, x, y, w, h, a))
    return lista_baloes

def draw():
    global f
    background(128)
    t = 1 - abs(sin(radians(f)))
    for i, (a, b) in enumerate(zip(lista_baloes, lista_proximos))  :
        # lista_baloes[i] = lerp_balao(a, b, float(mouseX) / width)
        cor, x, y, w, h, ang = lerp_balao(a, b, t)
        # cor, x, y, w, h, ang = lerp_balao(a, b, map(mouseX, 0, width, 0, 1))
        stroke(cor)
        draw_poly(balao(x, y, w, h, angle=ang))

    global lista_baloes, lista_proximos
    if f % 180 == 0: 
        lista_baloes = cria_baloes()
    f += 0.5


def lerp_balao(a, b, t):
    cor = [lerpColor(a[0], b[0], t)]
    other = [lerp(aa, bb, t) for aa, bb in zip(a[1:], b[1:])]
    return tuple(cor + other)
            
def balao(ox, oy, w, h, ponta=None, mode=CENTER, angle=None):
    wbase = w / 4
    offset = w / 4
    if mode == CENTER:
        x, y = ox - w / 2.0, oy - h / 2.0
    else:
        x, y = ox, oy
    px, py = ponta or x + w, y + h * 1.5
    
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
        global lista_baloes, lista_proximos
        lista_baloes = cria_baloes()
