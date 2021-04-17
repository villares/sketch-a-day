# Inspired by a chat with twitter.com/arturched

wm, hm = 20, 20 # dimensoes elemento    
num_areas = 7
num_elementos = 200

def setup():
    global areas_a, areas_b
    global elementos_a, elementos_b
    size(700, 700)
    fill(255)
    noStroke()
    areas_a = sorted(sorteia_areas(), key=lambda a:a[1])
    areas_b = sorted(sorteia_areas(), key=lambda a:a[1])
    elementos_a = sorted(sorteia_elementos(areas_a), key=lambda a:a[1])
    elementos_b = sorted(sorteia_elementos(areas_b), key=lambda a:a[1])
    
def draw():
    background(200)
    # desenha_areas(areas_a)
    # desenha_elementos(elementos_a)
    t = map(mouseX, 0, width, 0, 1)
    areas = lerp_multiplo(areas_a, areas_b, t)
    elementos = lerp_multiplo(elementos_a, elementos_b, t)
    desenha_areas(areas)
    desenha_elementos(elementos)
    
def sorteia_areas():
    areas = []
    # sorteia as areas
    while len(areas) < num_areas:
        xa, ya = random(width), random(height)
        wa, ha = random(240, 500) // 10 * 10, random(40, 140) // 10 * 10
        if in_area(xa, ya, wa, ha, 0, 0, width, height):
            if not sobrepondo_na_colecao(xa, ya, wa, ha, areas):
                areas.append((xa + 2, ya + 2, wa - 4, ha - 4))
    return areas

def desenha_areas(areas):
    fill(255)
    for x, y, w, h in areas:
        rect(x, y, w, h)        

def sorteia_elementos(areas):
    elementos = []
    while len(elementos) < num_elementos:
        xm, ym = random(width) // 10 * 10, random(height) // 10 * 10
        for xa, ya, wa, ha in areas:
            if in_area(xm, ym, wm, hm, xa, ya, wa, ha):
                if not sobrepondo_na_colecao(xm, ym, wm, hm, elementos):
                    elementos.append((xm + 2, ym + 2,
                                      wm - 4, hm - 4))
                    break
    return elementos

def desenha_elementos(elementos):
    fill(0)   
    for x, y, w, h in elementos:
        rect(x, y, w, h)

def lerp_multiplo(a, b, t):
    return tuple(tuple(lerp(ea, eb, t) for ea, eb in zip(aa, ab))
                                       for aa, ab in zip(a, b))
                        
def in_area(xm, ym, wm, hm, xa, ya, wa, ha):
    return (xa < xm < xa + wa - wm and
            ya < ym < ya + ha - hm)

def rect_on_rect(r1x, r1y, r1w, r1h, r2x, r2y, r2w, r2h):
    # via http://jeffreythompson.org/collision-detection/rect-rect.php
    return (r1x + r1w >= r2x and    # r1 right edge past r2 left
            r1x <= r2x + r2w and          # r1 left edge past r2 right
            r1y + r1h >= r2y and          # r1 top edge past r2 bottom
            r1y <= r2y + r2h) 

def sobrepondo_na_colecao(x, y, w, h, colecao):
    for ox, oy, ow, oh in colecao:
        if rect_on_rect(x, y, w, h,
                        ox, oy, ow, oh):
            return True
    return False


            
