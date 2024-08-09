# from itertools import product

# You'll need py5 and a use the run_sketch tool or Thonny + thonny-py5mode
# to run this py5 "imported mode" style sketch. Learn more at py5coding.org

def setup():
    size(600, 600)
    rect_mode(CENTER)
    color_mode(HSB)
    no_stroke()
    
def draw():
    background(0)
    w = 140
    for x in range(5):
        for y in range(5):
            unit(x * w,
                 y * w, w)
        
def unit(x, y, w):
    # w = r * 2 + r * 2 / (1 + sqrt(2))
    r = w / (2 * sqrt(2))  # octagon inradius
    s = r * 2 / (1 + sqrt(2)) # square side
    # square(x, y, w)  # visual debug
    offset = - r * sqrt(2) / 2
    poly(x + offset, y + offset, r)
    poly(x + r + s / 2 + offset,
           y + offset, s, n=4)
    poly(x + w / 2 + offset, y + w / 2 + offset, r)
    poly(x - r - s / 2 + w / 2 + offset,
           y + w / 2 + offset, s, n=4)
    # circle(x, y, 5)  # visual debug
    
    
def poly(x, y, r, n=8, rot=0):
    if n == 8:
        r = r / cos(PI / 8) # circumradius
    if n == 4:
        r = r * sqrt(2) / 2
    poly_pts = []
    ang = TWO_PI / n
    for i in range(n):
        sx = x + cos(i * ang + ang / 2 + rot) * r
        sy = y + sin(i * ang + ang / 2 + rot) * r
        poly_pts.append((sx, sy))
    for a, b, c in triangulate(poly_pts):
        for sa, sb, sc in triangulate((a, b, c)):
            fill(64 + sa[0] % 128, 255, 128 + sb[1]  % 128)
            triangle(*sa, *sb, *sc)
#             for ssa, ssb, ssc in triangulate((sa, sb, sc)):
#                     triangle(*ssa, *ssb, *ssc)

def key_pressed():
    save_frame('out.png')
            
def triangulate(pts):
    xs, ys = tuple(zip(*pts))
    xc, yc = sum(xs) / len(xs), sum(ys) / len(ys)
    triangles = []
    for i, (x, y) in enumerate(pts):
        x0, y0 = pts[i-1]
        triangles.append(((x, y), (x0, y0), (xc, yc)))
    return triangles


