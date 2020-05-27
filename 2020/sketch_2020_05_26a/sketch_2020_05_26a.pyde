# A Processing map() demo!
# Based on an idea from John @introscopia
# + arrowhead by John

X1, X2 = 133, 266
drag = -1
y_off = 100
names = True

def setup():
    size(400, 400)
    strokeWeight(3)
    f = createFont('Inconsolata Bold', 10)
    textFont(f)
    init_pts()

def init_pts():
    global pts
    pts = [80, 40, 120, 5, 250]  # a, si, sf, ti, tf

def draw():
    background(240)
    translate(0, y_off)
    a = pts[0]
    b = map(a, pts[1], pts[2], pts[3], pts[4])

    if names:
        txt = ('a', 'a0', 'a1', 'b0', 'b1')
        ta = 'a'
        tb = 'b'
    else:
        ta = 'a:{}'.format(a)
        tb = 'b:{:.4f}'.format(b)
        txt = pts

    fill(0)
    stroke(0, 200, 0)
    bar(X1, pts[1], X1, pts[2], txt[1], txt[2], RIGHT, RIGHT)
    stroke(100, 0, 100)
    bar(X2, pts[3], X2, pts[4], txt[3], txt[4], LEFT, LEFT)
    stroke(0)
    bar(X1, a, X2, b, ta, tb, RIGHT, LEFT)

    textAlign(CENTER)
    caption = 'b = map({}, {}, {}, {}, {})'.format(*txt)
    textSize(18)
    text(caption, width / 2, 40 - y_off)

def mousePressed():
    global drag
    for i, pt in enumerate(pts):
        if i < 3 and dist(X1, pt, mouseX, mouseY - y_off) < 5:
            drag = i
            return
        elif dist(X2, pt, mouseX, mouseY - y_off) < 5:
            drag = i
            return

def mouseDragged():
    if drag >= 0:
        pts[drag] = mouseY - y_off

def mouseReleased():
    global drag
    drag = -1

def keyPressed():
    global names
    if key == ' ':
        init_pts()
    if keyCode == SHIFT:
        names = not names

def bar(x1, y1, x2, y2, t1=None, t2=None, a1=None, a2=None):
    push()
    line(x1, y1, x2, y2)
    if t1:
        if a1:
            textAlign(a1, CENTER)
        text(' {} '.format(t1), x1, y1)
    if t2:
        if a2:
            textAlign(a2, CENTER)
        text(' {} '.format(t2), x2, y2)
    fill(255)
    circle(x1, y1, 10)
    if a1 == RIGHT and a2 == LEFT:
        fill(0)
        translate(x2, y2)
        a = atan2(y2 - y1, x2 - x1)
        rotate(a)
        strokeJoin(ROUND)
        strokeWeight(1)
        triangle(0, 0, -12, -5, -12, 5)
    else:
        circle(x2, y2, 10)
    pop()
