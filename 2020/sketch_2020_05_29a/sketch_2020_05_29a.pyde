# A Processing lerpColor() demo!
# Based on an idea from John @introscopia

X1, X2 = 120, 200
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
    c0 = color(random(256), random(256), random(256))
    c1 = color(random(256), random(256), random(256))
    pts = [100, 50, 150, c0, c1]

def draw():
    global b
    background(240)
    translate(0, y_off)
    a = map(pts[0], pts[1], pts[2], 0, 1)

    b = lerpColor(pts[3], pts[4], a)
    txt = ['t', '(0%) 0', '(100%) 1', 'c0', 'c1', 'c']
    if names:
        ta = 't'
        tb = '   c'
    else:
        ta = 't:{:.2f}'.format(a)
        tb = '    c:color({:.0f}, {:.0f}, {:.0f})'.format(
            red(b), green(b), blue(b))
        txt[0] = '{:.2f}'.format(a)
        txt[3:5] = ('color({:.0f}, {:.0f}, {:.0f})'
                    .format(red(pts[3]), green(pts[3]), blue(pts[3])),
                    'color({:.0f}, {:.0f}, {:.0f})'
                    .format(red(pts[4]), green(pts[4]), green(pts[4])))
    near_a = .1
    near_b = .1  # abs(pts[3] - pts[4]) * near_a / 2

    a0 = '' if abs(a) < near_a else txt[1]
    a1 = '' if abs(a - 1) < near_a else txt[2]
    b0 = '' if abs(a) < near_b else txt[3]
    b1 = '' if abs(a - 1) < near_b else txt[4]

    textSize(18)
    fill(0)
    stroke(100)
    bar(X1, pts[1], X1, pts[2], a0, a1, RIGHT, RIGHT)
    right_labels(X2+26, pts[1], X2+26, pts[2], b0, b1)
    stroke(0)
    fill(pts[3])
    circle(X2, pts[1], 50)
    fill(pts[4])
    circle(X2, pts[2], 50)
    stroke(0)
    y2 = min(max(pts[0], pts[1]), pts[2])
    bar(X1, pts[0], X2, y2, ta, tb, RIGHT, LEFT)
    fill(0)
    if names:
        textAlign(CENTER)
        caption = '{} = lerpColor(c0, c1, t)'
        text(caption, width / 2, 40 - y_off)
    else:
        textSize(14)
        textAlign(LEFT)
        caption = ('{} = lerpColor({},\n'
                   '              {},\n'
                   '              {})'.format(txt[5], txt[3], txt[4], txt[0]))
        text(caption, width / 8, 40 - y_off)

def mousePressed():
    global drag
    if abs(pts[0] - (mouseY - y_off)) < 5:
        drag = 0

def mouseDragged():
    if drag == 0:
        pts[0] = mouseY - y_off

def mouseReleased():
    global drags
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
    fill(0)
    line(x1, y1, x2, y2)
    if not names and a1 == LEFT:
        textSize(12)
    textAlign(a1, CENTER)
    text(' {} '.format(t1), x1, y1)
    if not names and a2 == LEFT:
        textSize(12)
    textAlign(a2, CENTER)
    fill(0)
    text(' {} '.format(t2), x2, y2)
    fill(255)
    d = 3 if a1 == RIGHT and a2 == RIGHT else 10
    circle(x1, y1, d)
    if a1 == RIGHT and a2 == LEFT:
        fill(b)
        circle(x2, y2, 50)
    else:
        circle(x2, y2, d)
    pop()
    
def right_labels(x1, y1, x2, y2, t1, t2):
    fill(0)
    textAlign(LEFT, CENTER)
    if not names:
        textSize(12)
    text(' {} '.format(t1), x1, y1)
    text(' {} '.format(t2), x2, y2)
    
