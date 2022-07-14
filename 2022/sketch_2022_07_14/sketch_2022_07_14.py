L = 26
H = L * sqrt(3) / 2

def setup():
    size(800, 800)
    background(255)
    translate(width / 2, height / 2)
    for k in range(6):
        base_y = H
        for i in range(1, 20):
            for j in range(-i + 1, i, 2):
                fill(128 * (j % 3), 128 * (i % 3), 128 * ((i + j) % 3))
                tile(i * 1.5 * L, base_y + j * H, L)
        rotate(TWO_PI / 6)
#     from villares.helpers import save_png_with_src
#     save_png_with_src()
  
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
    