L = 20
H = L * sqrt(3) / 2

from villares import arcs

def setup():
    size(800, 800)
    background(0)
    translate(width / 2, height / 2)
    for k in range(6):
        base_y = H
        for i in range(1, 20):
            for j in range(-i + 1, i, 2):
                stroke(0)
                stroke_weight(2)
                fill(128 + (abs(i + j) % 8) * 16 , 150)
                tile(i * 1.5 * L, base_y + j * H, L, radius=4 - sqrt(i*abs(j)))
        rotate(TWO_PI / 6)
    from villares.helpers import save_png_with_src
    save_png_with_src()
  
def tile(xc, yc, L, radius=15):
    with push():
        translate(xc, yc)
        for a in range(-1, 2): 
            rot = radians(60) * a
            pts = [(0, 0)]
            for i in (2, 3, 4):
                if i % 2 == 0:
                    r = L
                else:
                    r =  L * sqrt(3) # (L√3)/2 * 2
                ang = i * radians(30) + PI + rot
                x = r * cos(ang)
                y = r * sin(ang)
                pts.append((x, y))
            arcs.arc_augmented_poly(pts, radius=radius)
    
