# install PeasyCam lib with Import Library... > Add Libray... panel
add_library('peasycam') # add using your Processing IDE

cols = rows = 30
w = 20
z_off = 380

def setup():
    global surface_a, surface_b
    size(500, 500, P3D)
    cam = PeasyCam(this, 800)
    generate_surfaces()
    
def generate_surfaces():
    global surface_a, surface_b, vertical_faces
    noiseSeed(int(random(1000)))
    surface_a = []
    surface_b = []
    vertical_faces = []
    for i in range(cols):
        x = (i - cols / 2.0 + 0.5) * w
        for j in range(rows):
            y = (j - cols / 2.0 + 0.5) * w
            z =  (z_off - dist(x, y, 0, 0)) * 1
            n = noise(1000 + x * 0.01, 1000 + y * 0.01)
            p1 = (x, y, 150 * n)
            n = noise(100 + x * 0.03, y * 0.03)
            p2 = (x, y, -z - 50 * n)
            surface_a.append(p1)
            surface_b.append(p2)
        
    pairs = tuple(zip(surface_a, surface_b))
    fa = vertical_face(pairs[-cols:])
    vertical_faces.append(fa)
    fa = vertical_face(pairs[:cols])
    vertical_faces.append(fa)
    fa = vertical_face(pairs[::cols])
    vertical_faces.append(fa)
    fa = vertical_face(pairs[cols-1::cols])
    vertical_faces.append(fa)
                                 
                                                                                            
def draw():
    background(200, 220, 240)
    ambientLight(130, 130, 130)
    directionalLight(255, 255, 200, 1, 1, -0.5)
    strokeWeight(1)
    for i, face in enumerate(vertical_faces):
        fill(i * 64, 255 - i * 64, 255)
        draw_face(face)
    fill(255)    
    strokeWeight(0.5)
    draw_surface(surface_a)
    draw_surface(surface_b)
        
def draw_surface(surface):
    for r in range (rows - 1):
        for c in range (cols - 1):
            p1 = surface[r * cols + c]
            p2 = surface[r * cols + c + 1]
            p3 = surface[(r + 1) * cols + c + 1]
            p4 = surface[(r + 1) * cols + c]
            draw_face((p1, p2, p3))
            draw_face((p3, p4, p1))
            
def draw_face(points):
    beginShape()
    for x, y, z in points:
        vertex(x, y, z)
    endShape(CLOSE)
            
def vertical_face(pairs):
    return  tuple([p1 for p1, p2 in pairs] +
                  [p2 for p1, p2 in reversed(pairs)])
    
def keyPressed():
    # if key == 'r':
        print('oi')
        generate_surfaces()
