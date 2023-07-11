# 3D studies with Julio Mariutti 
# inspired by: https://seoi.net/peni3d/
# Converting sketch_2020_12_17a_3D_revolve to py5.


pts = []
rot_y = 0
meridians = 24

def setup():
    size(500, 500, P3D)
    stroke_weight(2)
    no_fill()
    color_mode(HSB)

def draw():
    global tmouse_x, tmouse_y
    translate(width / 2, height / 2)
    tmouse_x, tmouse_y = mouse_x - width / 2, mouse_y - width / 2
    rotate_y(rot_y)
    background(0)
    
    pm = int(len(pts) / 2)  # indice do ponto medio
    # if pm > 0:
    #     circle(pts[pm][0], pts[pm][1], 15)
    # for p in pts:
    #     circle(p[0], p[1], 5)
    
    paralelos = []
    mx, my = 0, 0  # middle
    for a, b in zip(pts[:pm], pts[-1:pm - 1:-1]):
        d = dist(a[0], a[1], b[0], b[1])  # diameter
        mx, my = (a[0] + b[0]) / 2.0, (a[1] + b[1]) / 2.0
        ang = atan2(b[1] - a[1], b[0] - a[0]) + PI
        circulo = [rotate_p(x, y, ang, mx, my) + (z, )
                   for x, y, z in z_circle(mx, my,
                                           d / 2.0,
                                           num_pts=meridians)]
        paralelos.append((d, circulo))  # diameter will be used later for stroke color

    for d, circulo in paralelos:    # diameter, circle_pts
        stroke(d % 256, 255, 255)
        with begin_closed_shape():
            vertices(circulo)
        
        
    stroke(128)
    for i in range(meridians):
        begin_shape()
        for _, circulo in paralelos:
            x, y, z = circulo[i]
            vertex(x, y, z)
        vertex(mx, my, 0)
        end_shape()

    stroke(255)    
    begin_shape()
    for p in pts:
        vertex(p[0], p[1], 0)
    end_shape()

def mouse_pressed():
    pts[:] = []
    pts.append((tmouse_x, tmouse_y))

def mouse_dragged():
    if dist(tmouse_x, tmouse_y,
            pts[-1][0], pts[-1][1]) > 15:
        pts.append((tmouse_x, tmouse_y))

def key_pressed():
    global rot_y
    if key_code == LEFT:
        rot_y -= radians(5)
    if key_code == RIGHT:
        rot_y += radians(5)
    if key == ' ':
        rot_y = 0

def z_circle(x, y, radius, num_pts=16):
    a = TWO_PI / num_pts
    return tuple((x + cos(a * i) * radius, y, sin(a * i) * radius)
                  for i in range(num_pts))

def rotate_p(xp, yp, angle, x0=0, y0=0):
    x, y = xp - x0, yp - y0  # translate to origin
    xr = x * cos(angle) - y * sin(angle)
    yr = y * cos(angle) + x * sin(angle)
    return (xr + x0, yr + y0)


