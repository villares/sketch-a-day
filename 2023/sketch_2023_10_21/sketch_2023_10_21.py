from triangulate import triangulate

MINIMUM_DIST = 50

poly = []
tris = []

def setup():
    size(600, 600)
    
def draw():
    background(200)
    stroke(0)
    stroke_weight(5)
    no_fill()
    points(poly)
    
    if len(poly) > 3:
        tris[:] = triangulate(poly)
    for t in tris:        
        stroke(255)
        stroke_weight(1)
        fill(255, 100)
        begin_shape()
        vertices(t)
        end_shape(CLOSE)

        
def mouse_dragged():
    # adds a tuple with the mouse coordinates if the poly list is empty
    # or if the x, y in poly[-1] are far enough from the mouse
    if not poly or dist(poly[-1][0], poly[-1][1], mouse_x, mouse_y) > MINIMUM_DIST:
        poly.append((mouse_x, mouse_y))    

#     if not poly:
#         poly.append((mouse_x, mouse_y))
#         return
#     px, py = poly[-1]
#     if dist(px, py, mouse_x, mouse_y) > MINIMUM_DIST:
#         poly.append((mouse_x, mouse_y))


    
def key_pressed():
    poly[:] = []
