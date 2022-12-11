from villares.arcs import arc_filleted_poly


def setup():
    size(800, 800)
    
        
def draw():
    background(240)
    no_fill()
    p_list = [(30, 160), (250, 50), (350, 150), (mouse_x, mouse_y)]
    stroke(200, 0, 0)
    stroke_weight(4)
    arc_filleted_poly(p_list, radius=500)  # arc_func=b_arc by default
    stroke(0)
    stroke_weight(1)
    with begin_shape():
        vertices(p_list)
    stroke(0, 0, 200)
    stroke_weight(2)
    arc_filleted_poly(p_list, radius=500, open_poly=True)
