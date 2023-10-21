from triangulate import triangulate

poly = []
tris = []

def setup():
    size(600, 600)
    
def draw():
    background(200)
    stroke(0)
    stroke_weight(5)
    no_fill()
    begin_shape()
    vertices(poly)
    end_shape(CLOSE)
    
    if len(poly) > 3:
        tris[:] = triangulate(poly)
    for t in tris:        
        stroke(255)
        stroke_weight(1)
        fill(255, 100)
        begin_shape()
        vertices(t)
        end_shape(CLOSE)

        
def mouse_pressed():
    poly.append((mouse_x, mouse_y))
    #print(tris)

def key_pressed():
    poly[:] = []
