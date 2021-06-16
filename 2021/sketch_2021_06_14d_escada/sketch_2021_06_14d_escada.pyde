from villares.line_geometry import draw_poly

def setup():
    size(600, 600, P3D)
    
def draw():
    background(100)
    translate(300, 300)
    if mousePressed:
        rotateY(mouseX / 100.0)
    translate(-150, -150)
    face_a = stair_face(10, 30, 30, 5, 0)
    draw_poly(face_a)
    face_b = stair_face(10, 30, 30, 30, 100)
    draw_poly(face_b)

    for pair_a, pair_b in zip(edge_pair(face_a), edge_pair(face_b)):
        p1, p2 = pair_a
        p3, p4 = pair_b
        beginShape()
        vertex(*p1)
        vertex(*p2)
        vertex(*p4)
        vertex(*p3)
        endShape(CLOSE)    
        
def edge_pair(poly_points):
    return zip(poly_points,
               poly_points[1:] + [poly_points[0]])

def stair_face(num_degraus, pisada, espelho, espessura, z):
        pontos = []
        x = y = 0
        for _ in range(num_degraus):
            pontos.append((x, y, z))
            pontos.append((x + pisada, y, z))
            x += pisada
            y += espelho 
        pontos.append((x, y, z))
        x -= espessura
        pontos.append((x, y, z))
        y -= (espelho - espessura)
        for _ in range(num_degraus - 1):
            pontos.append((x, y, z))
            pontos.append((x - pisada, y, z))
            x -= pisada
            y -= espelho 
        pontos.append((x, y, z))
        pontos.append((x - pisada + espessura, y, z))
        return pontos
