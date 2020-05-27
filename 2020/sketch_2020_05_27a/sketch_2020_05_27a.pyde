# A Processing lerp() demo!
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
    pts = [70, 50, 150, 10, 220]

def draw():
    background(240)
    translate(0, y_off)
    a = map(pts[0], pts[1], pts[2], 0, 1)

    b = lerp(pts[3], pts[4], a)
    txt = ['t', '(0%) 0', '(100%) 1', 'v0', 'v1', 'v']
    if names:
        ta = 't'
        tb = 'v'
    else:
        ta = 't:{:.2f}'.format(a)
        tb = 'v:{:.2f}'.format(b)
        txt[0] = '{:.2f}'.format(a)
        txt[3:5] = pts[3], pts[4]

    near_a = .1
    near_b = abs(pts[3] - pts[4]) * near_a / 2

    a0 = '' if abs(a) < near_a else txt[1]
    a1 = '' if abs(a - 1) < near_a else txt[2]
    b0 = '' if abs(b - pts[3]) < near_b else txt[3]
    b1 = '' if abs(b - pts[4]) < near_b else txt[4]

    fill(0)
    stroke(0, 200, 0)
    bar(X1, pts[1], X1, pts[2], a0, a1, RIGHT, RIGHT)
    stroke(100, 0, 100)
    bar(X2, pts[3], X2, pts[4], b0, b1, LEFT, LEFT)
    stroke(0)
    bar(X1, pts[0], X2, b, ta, tb, RIGHT, LEFT)

    textAlign(CENTER)
    caption = '{} = lerp({}, {}, {})'.format(txt[5], txt[3], txt[4], txt[0])
    textSize(18)
    text(caption, width / 2, 40 - y_off)

def mousePressed():
    global drag
    for i, pt in enumerate(pts):
        if i == 0 and dist(X1, pt, mouseX, mouseY - y_off) < 5:
            drag = i
            return
        elif i > 2 and dist(X2, pt, mouseX, mouseY - y_off) < 5:
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

    if key == 'z':
        pts[0] += 1
    if key == 'a':
        pts[0] -= 1
    if key == 'x':
        pts[3] += 1
    if key == 's':
        pts[3] -= 1


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
    d = 3 if a1 == RIGHT and a2 == RIGHT else 10
    circle(x1, y1, d)
    if a1 == RIGHT and a2 == LEFT:
        fill(0)
        translate(x2, y2)
        a = atan2(y2 - y1, x2 - x1)
        rotate(a)
        strokeJoin(ROUND)
        strokeWeight(1)
        triangle(0, 0, -12, -5, -12, 5)
    else:
        circle(x2, y2, d)
    pop()
