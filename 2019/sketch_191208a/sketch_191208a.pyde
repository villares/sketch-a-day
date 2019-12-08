from __future__ import division
add_library('peasycam')

pontos = [[], []]  # duas listas para armazenar tuplas (x, y)
arrastando = [-1, -1]  # -1 significa nenhom ponto arrastado
offset_curva = [35, 5]

def setup():
    size(500, 500, P3D)
    background(240, 250, 250)
    pontos[1][:] = pontos[0][:] = sorteia_pontos(5)
    cam = PeasyCam(this, 500)
    cam.setMinimumDistance(500)
    cam.setMaximumDistance(500)
    orbitDH = cam.getRotateDragHandler(); # get the RotateDragHandler
    cam.setCenterDragHandler(orbitDH);                     # set it to the Center/Wheel drag
    panDH = cam.getPanDragHandler();      # get the PanDragHandler
    cam.setRightDragHandler(orbitDH);                        # set it to the right-button mouse drag
    cam.setLeftDragHandler(None);                          # sets no left-drag Handler


def sorteia_pontos(num):
    pontos = []
    for _ in range(num):
        x = random(-width * .4, width * .4)
        y = random(-height * .4, height * .4)
        pontos.append((x, y))
    return pontos

def draw():
    global mx, my
    mx, my = mouseX - width / 2, mouseY - width / 2
    # ortho()
    oc = offset_curva[0]
    background(240, 250, 250)
    last = 10
    for i in range(last):
        translate(0, 0, 10)
        pts = lerp_pts(pontos[0], pontos[1], i / last)
        oc = lerp(offset_curva[0], offset_curva[1], i / last)
        draw_pontos(pts, oc, i in (0, last - 1))

def draw_pontos(pontos, offset, handle=False):
    for i, (x0, y0) in enumerate(pontos):
        x1, y1 = pontos[i - 1]
        noFill()
        stroke(0)
        strokeWeight(2)
        curva(x0, y0, x1, y1, offset, d=True)
        if handle and dist(mx, my, x0, y0) < 10:
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

def lerp_pts(pts1, pts2, a):
    if a == 0:
        return pts1
    if a == 1:
        return pts2
    if len(pts1) == 2:
        return (lerp(pts1[0], pts2[0], a),
                lerp(pts1[1], pts2[1], a))
    pts = []
    for p1, p2 in zip(pts1, pts2):
        pts.append(lerp_pts(p1, p2, a))
    return pts

def mousePressed():
    for i, (x0, y0) in enumerate(pontos[1]):
        if dist(mx, my, x0, y0) < 50:
            arrastando[1] = i
            return
    for i, (x0, y0) in enumerate(pontos[0]):
        if dist(mx, my, x0, y0) < 50:
            arrastando[0] = i

def mouseReleased():
    arrastando[:] = [-1, -1]

def mouseDragged():
    if arrastando[0] >= 0:
        pontos[0][arrastando[0]] = (mx, my)
    if arrastando[1] >= 0:
        pontos[1][arrastando[1]] = (mx, my)

def mouseWheel(e):
    if keyCode == SHIFT and keyPressed:
        offset_curva[1] += e.getCount() / 5.
    else:
        offset_curva[0] += e.getCount() / 5.

def keyPressed():
    if key == ' ':
        pontos[0][:] = pontos[1][:] = sorteia_pontos(5)
    if key == 's':
        saveFrame("####.png")
