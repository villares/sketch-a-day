from itertools import chain

def setup():
    size(600, 600)
    first_triangle()
    
def first_triangle():
    global tris
    R, cx, cy = 300, width / 2, height * 0.60
    first_triangle = []
    for i in range(3):
        a = i * TWO_PI / 3 - TWO_PI / 4        x = cx + R  * cos(a)
        y = cy + R  * sin(a)
        first_triangle.append((x, y))
    tris = [tuple(first_triangle)]

def draw():
    background(0)
    no_fill()
    for (va, vb, vc), (vd, ve, vf) in zip(tris, reversed(tris)):
        stroke((va[0] * va[1]) % 255, vd[0] % 255, vd[1] % 255, 100)
        #triangle(*va, *vb, *vc)
        line(*va, *vd)
        
def key_pressed():
    if key == ' ':
        tris[:] = divide_triangles(tris)
    elif key == 'n':
        first_triangle()
        
def divide_triangles(triangles):
    return chain.from_iterable(divide_triangle(tri) for tri in triangles)
    
def divide_triangle(tri):
    r = 0.5
    (vax, vay), (vbx, vby), (vcx, vcy) = a, b, c = tri
    mab = lerp(vax, vbx, r), lerp(vay, vby, r)
    mcb = (vcx + vbx) / 2, (vcy + vby) / 2
    mac = (vax + vcx) / 2, (vay + vcy) / 2
    return (a, mac, mab), (mcb, b, mab), (mcb, mac, c)
