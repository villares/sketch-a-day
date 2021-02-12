# after exploring and debugging with Daniel Bueno!

from villares.line_geometry import draw_poly, rotate_point
from random import choice

add_library('peasycam')  # é preciso baixar/instalar pelo IDE

cores = (color(200, 0, 0),
         color(255),
         color(0) )
f = 0 

def setup():
    size(500, 500, P3D)
    cam = PeasyCam(this, height * 1.5)
    # cam.setMinimumDistance(100)
    # cam.setMaximumDistance(200)   
    strokeWeight(5)
    noFill()
    global lista_shapes, lista_proximos
    lista_shapes = cria_shapes()
    lista_proximos = cria_shapes()
    textAlign(CENTER)
    textMode(SHAPE)
    fonte = createFont("Tomorrow Bold", 18)
    textFont(fonte)    
    
def cria_shapes(n=3):
    lista_shapes = []
    while len(lista_shapes) < n:
        cor = choice(cores)
        x = choice(range(175, width - 175, 25))
        y = choice(range(175, width - 175, 25))
        w = choice((-300, -200, 200, 300))
        h = choice((250, 200, 150, 100))
        ang = choice((0, 0, 0, HALF_PI, -HALF_PI))
        px, py = forma(x, y, w, h, angle=ang)[4]
        forma_bom = True
        for b in lista_shapes:
            pobx, poby = b[-2], b[-1]
            if dist(pobx, poby, px, py) < 300:
                forma_bom = False
        if forma_bom:
            lista_shapes.append((cor, x, y, w, h, ang, px, py))            
    return lista_shapes

def draw():
    global f
    # background(128)
    background(64, 128, 200)
    translate(-width / 2, -height / 2)
    # pushMatrix()
    # t = 1 - abs(sin(radians(f)))
    t = map(mouseX, 0, width, 0, 1)
    # t = 1
    for j in range(5):
      t = j / 9.0
      for i, (a, b) in enumerate(zip(lista_shapes, lista_proximos))  :
        # lista_shapes[i] = lerp_forma(a, b, float(mouseX) / width)
        cor, x, y, w, h, ang, px, py = lerp_forma(a, b, t)
        # cor, x, y, w, h, ang = lerp_forma(a, b, map(mouseX, 0, width, 0, 1))
        stroke(cor)
        j =  1
        translate(0, 0, x / 10)
        draw_poly(forma(x, y,  w * (1 - 0.20 * t * j),
                            h * (1 - 0.20 * t * j), angle=ang))
    # popMatrix()
    translate(0, 0, -40)
    for b in lista_shapes:  
        cor, x, y, w, h, ang, px, py = b
        for ob in lista_shapes:
            pobx, poby = ob[-2], ob[-1]
            stroke(0, 0, 200)
            strokeWeight(3)
            line(pobx, poby, px, py)
            # print(dist(pobx, poby, px, py)) 
        stroke(255)
        strokeWeight(5)
        pontos_forma = forma(x, y, w, h, angle=ang)
        draw_poly(pontos_forma) 
        fill(0)
        translate(0, 0, 2)
        for i, (pbx, pby) in enumerate(pontos_forma):
            text(str(i), pbx, pby)        
        noFill()


    # global lista_shapes, lista_proximos
    # if f % 180 == 0: 
    #     lista_shapes = cria_shapes()
    # f += 0.5


def lerp_forma(a, b, t):
    cor = [lerpColor(a[0], b[0], t)]
    other = [lerp(aa, bb, t) for aa, bb in zip(a[1:], b[1:])]
    return tuple(cor + other)
            
def forma(ox, oy, w, h, ponta=None, mode=CENTER, angle=None):
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
        global lista_shapes, lista_proximos
        lista_shapes = cria_shapes()
