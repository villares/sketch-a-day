# A Processing PVector.lerp() demo!
# Based on an idea from John @introscopia
# + arrowhead by John

"""
Can we interpolate a vector? Sure, there is a PVector method for that!
"""

X1, X2 = 120, 240
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
    pts = [70, 50, 150, PVector(X2, 10), PVector(X2, 220)]

def draw():
    background(240)
    translate(0, y_off)
    a = map(pts[0], pts[1], pts[2], 0, 1)

    b = PVector.lerp(pts[3], pts[4], a)
    txt = ['t', '(0%) 0', '(100%) 1', 'v0', 'v1', 'v']
    if names:
        ta = 't'
        tb = 'v'
    else:
        ta = 't:{:.2f}'.format(a)
        tb = 'v:PVector({:.1f}, {:.1f})'.format(b.x, b.y)
        txt[0] = '{:.2f}'.format(a)
        txt[3:5] = (' v0:PVector({:.1f}, {:.1f})'.format(pts[3].x, pts[3].y),
                    ' v1:PVector({:.1f}, {:.1f})'.format(pts[4].x, pts[4].y)) 
    near_a = .1
    near_b = .1 # abs(pts[3] - pts[4]) * near_a / 2

    a0 = '' if abs(a) < near_a else txt[1]
    a1 = '' if abs(a - 1) < near_a else txt[2]
    b0 = '' if dist(b.x, b.y, pts[3].x, pts[3].y) < near_b else txt[3]
    b1 = '' if dist(b.x, b.y, pts[4].x, pts[4].y) < near_b else txt[4]

    textSize(18)
    fill(0)
    stroke(0, 200, 0)
    bar(X1, pts[1], X1, pts[2], a0, a1, RIGHT, RIGHT)
    stroke(100, 0, 100)
    bar(pts[3].x, pts[3].y, pts[4].x, pts[4].y, b0, b1, LEFT, LEFT)
    stroke(0)
    bar(X1, pts[0], b.x, b.y, ta, tb, RIGHT, LEFT)

    if names:
        textAlign(CENTER)
        caption = ('{} = PVector.lerp({}, {}, {})'
                   .format(txt[5], txt[3], txt[4], txt[0]))
        text(caption, width / 2, 40 - y_off)

    else:
        textSize(14)
        textAlign(LEFT)
        caption = ('{} = PVector.lerp({},\n'
                   '                 {},\n'
                   '                  {})'.format(txt[5], txt[3], txt[4], txt[0]))
        text(caption, width / 8, 40 - y_off)

def mousePressed():
    global drag
    for i, pt in enumerate(pts):
        if i == 0 and dist(X1, pt, mouseX, mouseY - y_off) < 5:
            drag = i
            return
        elif i > 2 and dist(pt.x, pt.y, mouseX, mouseY - y_off) < 5:
            drag = i
            return

def mouseDragged():
    if drag >= 0:
        if drag == 0:
            pts[drag] = mouseY - y_off
        else: 
            pts[drag] = PVector(mouseX, mouseY - y_off)    

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


def bar(x1, y1, x2, y2, t1, t2, a1, a2):
    push()
    line(x1, y1, x2, y2)
    if not names and a1 == LEFT:
        textSize(12)
    textAlign(a1, CENTER)
    text(' {} '.format(t1), x1, y1)
    if not names and a2 == LEFT:
        textSize(12)
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
