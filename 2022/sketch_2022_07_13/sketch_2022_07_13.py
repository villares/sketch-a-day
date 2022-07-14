L = 50
H = L * sqrt(3) / 2

def setup():
    size(800, 800)
    background(64)
    translate(width / 2, height / 2)   
    for _ in range(6):
        fill(200, 200, 0)
        tile(1.5 * L, H, L)
        fill(255, 100, 0)
        tile(4.5 * L, H, L)
        fill(0, 100, 200)
        tile(3 * L, 0 * H, L)
        tile(3 * L, 2 * H, L)
        fill(200)
        tile(4.5 * L,-1 * H, L)
        tile(4.5 * L, 3 * H, L)
        rotate(radians(60))
  
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
    