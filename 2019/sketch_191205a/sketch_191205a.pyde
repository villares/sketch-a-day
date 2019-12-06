
pontos = []
novos_pontos = []
arrastando = -1
offset_curva = 10
novo_offset_curva = 10

def setup():
    size(500, 500)
    background(240, 250, 250)
    novos_pontos[:] = pontos[:] = sorteia_pontos()

def sorteia_pontos():
    pontos = []
    for _ in range(5):
        x, y = random(width * .2, width * .8), random(height * .2, height * .8)
        pontos.append((x, y))
    return pontos

def draw():    
    background(240, 250, 250)
    for i in range(5):
        pts = lerp_pts(pontos, novos_pontos, i / 5.)
        draw_pontos(pts, offset_curva, handle=not i)    
 
def draw_pontos(pontos, offset, handle=False):
    for i, (x0, y0) in enumerate(pontos):
        x1, y1 = pontos[i - 1]
        noFill()
        stroke(0)
        strokeWeight(2)
        curva(x0, y0, x1, y1, offset, d=True)
        if handle and dist(mouseX, mouseY, x0, y0) < 10:
            stroke(255, 0, 0)
            strokeWeight(1)
            circle(x0, y0, 10)

def curva(x1, y1, x2, y2, offset=0, d=False):
    L = dist(x1, y1, x2, y2)
    if not d or L < 10 + abs(offset):
        with pushMatrix():
            translate(x1, y1)
            angle = atan2(x1 - x2, y2 - y1)
            rotate(angle)
            cx = (L / 2) * offset / 10.
            bezier(0, 0, -cx, L * .50, +cx, L * .50, 0, L)
    else:
        xm, ym = (x1 + x2) / 2, (y1 + y2) / 2
        curva(x1, y1, xm, ym, offset)
        curva(xm, ym, x2, y2, offset)

def lerp_pt(p1, p2, a):
    if a == 0: return p1
    if a == 1: return p2
    return (lerp(p1[0], p2[0], a), lerp(p1[1], p2[1], a))

def lerp_pts(pts1, pts2, a):
    if a == 0: return pts1
    if a == 1: return pts2
    pts = []
    for p1, p2 in zip(pts1, pts2):
        pts.append(lerp_pt(p1, p2, a))
    return pts
    
def mousePressed():
    global arrastando
    for i, (x0, y0) in enumerate(pontos):
        if dist(mouseX, mouseY, x0, y0) < 10:
            arrastando = i

def mouseReleased():
    global arrastando
    arrastando = -1

def mouseDragged():
    if arrastando >= 0:
        novos_pontos[arrastando] = (mouseX, mouseY)

def mouseWheel(e):
    global novo_offset_curva 
    novo_offset_curva += e.getCount() / 5.

def keyPressed():
    if key == ' ':
        pontos[:] = sorteia_pontos()
    if key == 's':
        saveFrame("####.png")
