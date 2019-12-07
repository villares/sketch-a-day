from __future__ import division

pontos0 = []
pontos1 = []
arrastando = [-1, -1]
offset_curva0 = 10
offset_curva1 = 10

def setup():
    size(500, 500)
    background(240, 250, 250)
    pontos1[:] = pontos0[:] = sorteia_pontos0()

def sorteia_pontos0():
    pontos0 = []
    for _ in range(5):
        x, y = random(width * .2, width * .8), random(height * .2, height * .8)
        pontos0.append((x, y))
    return pontos0

def draw():
    oc = offset_curva0

    background(240, 250, 250)
    last = 10
    for i in range(last):
        pts = lerp_pts(pontos0, pontos1, i / last)
        oc = lerp(offset_curva0, offset_curva1, i / last)
        draw_pontos(pts, oc, i in (0, last))


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
    if a == 0:
        return p1
    if a == 1:
        return p2
    return (lerp(p1[0], p2[0], a), lerp(p1[1], p2[1], a))

def lerp_pts(pts1, pts2, a):
    if a == 0:
        return pts1
    if a == 1:
        return pts2
    pts = []
    for p1, p2 in zip(pts1, pts2):
        pts.append(lerp_pt(p1, p2, a))
    return pts

def mousePressed():
    for i, (x0, y0) in enumerate(pontos1):
        if dist(mouseX, mouseY, x0, y0) < 10:
            arrastando[1] = i
            return
    for i, (x0, y0) in enumerate(pontos0):
        if dist(mouseX, mouseY, x0, y0) < 10:
            arrastando[0] = i

def mouseReleased():
    arrastando[:] = [-1, -1]

def mouseDragged():
    if arrastando[0] >= 0:
        pontos0[arrastando[0]] = (mouseX, mouseY)
    if arrastando[1] >= 0:
        pontos1[arrastando[1]] = (mouseX, mouseY)

def mouseWheel(e):
    global offset_curva0, offset_curva1
    if keyCode == SHIFT and keyPressed:
        offset_curva1 += e.getCount() / 5.
    else:
        offset_curva0 += e.getCount() / 5.

def keyPressed():
    if key == ' ':
        pontos0[:] = pontos1[:] = sorteia_pontos0()
    if key == 's':
        saveFrame("####.png")
