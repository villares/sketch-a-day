import py5

triangles = []

def setup():
    py5.size(800, 800)
    hw = py5.width / 2
    triangles[:] = triangulate([(
        (-hw, -hw), (hw, -hw), (hw, hw), (-hw, hw)
        )])
        
def draw():
    py5.translate(py5.width / 2, py5.height / 2)
    py5.background(0)
    py5.no_stroke()
    for a, b, c in triangles:
        py5.fill(100 + (a[0] + c[1]) % 155,
                 100 + (b[0] + a[1]) % 155,
                 100 + (c[0] + b[1]) % 155)
        py5.triangle(*a, *b, *c)

def key_pressed():
    if py5.key == ' ':
        py5.save_frame(f'{len(triangles):06}.png')
        triangles[:] = triangulate(triangles)

def triangulate(poly_sequence):
    triangles = []
    for pts in poly_sequence:
        xs, ys = tuple(zip(*pts))
        xc, yc = sum(xs) / len(xs), sum(ys) / len(ys)
        for i, (x, y) in enumerate(pts):
            x0, y0 = pts[i-1]
            triangles.append(((x, y), (x0, y0), (xc, yc)))
    return triangles

py5.run_sketch()