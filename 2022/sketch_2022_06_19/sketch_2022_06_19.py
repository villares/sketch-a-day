# Frank Morley's theorem demo

dragged = None
pts = [(100, 100), (300, 500), (500, 200)]
handle_radius = 10

def setup():
    size(600, 600)
    no_fill()
    
def draw():
    background(0, 0, 200)
    stroke(255)
    begin_shape()
    vertices(pts)
    end_shape(CLOSE)
    stroke(0)
    trissectors = []
    for i, (cx, cy) in enumerate(pts):
        px, py = pts[i - 1]
        nx, ny = pts[(i + 1) % len(pts)]
        start = atan2(cy - py, cx - px)
        angle = corner_angle((cx, cy), (px, py), (nx, ny))
        t1x = cos(start + angle / 3) * -1000 + cx
        t1y = sin(start + angle / 3) * -1000 + cy
        line(cx, cy, t1x, t1y)
        trissectors.append((cx, cy, t1x, t1y))
        t2x = cos(start + angle / 3 * 2) * -1000 + cx
        t2y = sin(start + angle / 3 * 2) * -1000 + cy
        line(cx, cy, t2x, t2y)
        trissectors.append((cx, cy, t2x, t2y)) 
    eq_pts = []
    for i, (x1, y1, x2, y2) in enumerate(trissectors):
        if i % 2 == 0:
            x3, y3, x4, y4 = trissectors[i - 1]
            eq_pts.append(line_intersect(x1, y1, x2, y2, x3, y3, x4, y4))
    stroke_weight(10)
    points(eq_pts)
    stroke_weight(1)
    for x, y in pts:
        circle(x, y, handle_radius * 2)
    
def corner_angle(corner, b, a):
    ac = atan2(a[1] - corner[1], a[0] - corner[0]) + PI
    bc = atan2(b[1] - corner[1], b[0] - corner[0]) + PI
    result = abs(ac - bc)
    return result if result <= PI else abs(result - TWO_PI)

def line_intersect(x1, y1, x2, y2, x3, y3, x4, y4):           
    divisor = (y4 - y3) * (x2 - x1) - (x4 - x3) * (y2 - y1)
    if divisor:
        uA = ((x4 - x3) * (y1 - y3) - (y4 - y3) * (x1 - x3)) / divisor
        uB = ((x2 - x1) * (y1 - y3) - (y2 - y1) * (x1 - x3)) / divisor
    else:
        return None
    # to check "in segment" if 0 <= uA <= 1 and 0 <= uB <= 1:
    x = x1 + uA * (x2 - x1)
    y = y1 + uA * (y2 - y1)
    return x, y

def mouse_pressed():
    global dragged
    for i, (x, y) in enumerate(pts):
        if dist(mouse_x, mouse_y, x, y) < handle_radius:
            dragged = i
            break

def mouse_dragged():
    print(dragged)
    if dragged is not None:
        dx, dy = mouse_x - pmouse_x, mouse_y - pmouse_y
        x, y = pts[dragged]
        pts[dragged] = (x + dx, y + dy)

def mouse_released():
    global dragged
    dragged = None


