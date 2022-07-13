
def setup():
    size(400, 400)
    background(0, 0, 200)
    fill(0, 200, 100)
    tile(200, 200, 100, - PI / 3)
    fill(100, 200, 0)
    tile(200, 200, 100, PI - PI / 3)   

def tile(xc, yc, L, rot=0):
    begin_shape()
    for i in range(7):
        if i % 2 == 0:
            r = L
        else:
            r =  L * sqrt(3) # (L√3)/2 * 2
        ang = i * radians(30) + PI + rot
        x = xc + r * cos(ang)
        y = yc + r * sin(ang)
        vertex(x, y)
    end_shape(CLOSE)