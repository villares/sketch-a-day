# Based on http://www.jeffreythompson.org/collision-detection/line-circle.php

r = 30         # circle radius
x1 = 100       # coordinates of line
y1 = 300
x2 = 500
y2 = 100

def setup():
    size(600,400)
    stroke_weight(5)
    
def draw():
    global cx, cy
    background(255)

    cx = mouse_x
    cy = mouse_y
    # if hit, change line's stroke color
    if line_circle(x1,y1, x2,y2, cx,cy,r):
        stroke(255,150,0, 150)
    else:
        stroke(0,150,255, 150)
    line(x1,y1, x2,y2)
    # draw the circle
    fill(0,150,255, 150)
    no_stroke()
    ellipse(cx,cy, r*2,r*2)

# LINE/CIRCLE
def line_circle(x1, y1, x2, y2, cx, cy, r):

    # is either end INSIDE the circle?
    # if so, return True immediately
    inside1 = point_circle(x1, y1, cx, cy, r)
    inside2 = point_circle(x2 ,y2, cx, cy ,r)
    if inside1 or inside2:
        return True

    # get line lenght
    dist_x = x1 - x2
    dist_y = y1 - y2
    ll = sqrt(dist_x ** 2 + dist_y ** 2)
    # get dot product of the line and circle
    dot = ((cx - x1) * (x2 - x1) + (cy - y1) * (y2 - y1)) / ll ** 2
    # find the closest point on the line
    closest_x = x1 + (dot * (x2 - x1))
    closest_y = y1 + (dot * (y2 - y1))

    # is this point actually on the line segment?
    # if so keep going, but if not, return False
    if not line_point(x1, y1, x2, y2, closest_x, closest_y):
        return False

    # optionally, draw a circle at the closest point on the line
    fill(255,0,0)
    no_stroke()
    ellipse(closest_x, closest_y, 20, 20)

    # get distance to closest point
    dist_x = closest_x - cx
    dist_y = closest_y - cy
    d = sqrt(dist_x ** 2 + dist_y ** 2)
    if d <= r:
        return True
    return False

def point_circle(x ,y, cx, cy ,r):
    return dist(x, y, cx, cy) <= r

def line_point(lax, lay, lbx, lby, px, py, tolerance=0.1):
    ab = dist(lax, lay, lbx, lby)
    pa = dist(lax, lay, px, py)
    pb = dist(px, py, lbx, lby)
    return (pa + pb) <= ab + tolerance
