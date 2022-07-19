from itertools import chain

tris = []

def setup():
    size(600, 600)
    R, cx, cy = 300, width / 2, height * 0.60
    first_triangle = []
    for i in range(3):
        a = i * TWO_PI / 3 - TWO_PI / 4
        x = cx + R  * cos(a)
        y = cy + R  * sin(a)
        first_triangle.append((x, y))
    tris.append(tuple(first_triangle))

def draw():
    background(0, 100, 0)
    no_stroke()
    for va, vb, vc in tris:
        triangle(*va, *vb, *vc)
        
def key_pressed():
    tris[:] = divide_triangles(tris)
    
def divide_triangles(triangles):
    return chain.from_iterable(divide_triangle(tri) for tri in triangles)
    
def divide_triangle(tri):
    (vax, vay), (vbx, vby), (vcx, vcy) = a, b, c = tri
    mab = (vax + vbx) / 2, (vay + vby) / 2
    mcb = (vcx + vbx) / 2, (vcy + vby) / 2
    mac = (vax + vcx) / 2, (vay + vcy) / 2
    return (a, mab, mac), (b, mab, mcb), (c, mac, mcb)
