
def setup():
    global f
    size(800, 400)
    color_mode(HSB)
    f = create_font('DejaVu Sans', 100)
    stroke_weight(3)
    frame_rate(5)
    
def draw():
    background(0)
    translate(10, 200)
    frase = 'Oi! Olá mundo...'
    x = 0
    no_fill()
    push_matrix()
    for c in frase:
        c_shp = f.get_shape(c, 1)
        vs3 = [c_shp.get_vertex(i) for i in range(c_shp.get_vertex_count())]        
        stroke(random(256), 255, 255)
        begin_shape()
        vs = set() 
        for x, y, _  in vs3:
            vertex(x, y)
            if (x, y) not in vs:
                vs.add((x, y))
            else:
                end_shape()
                stroke(random(256), 255, 255)
                begin_shape()
        end_shape()
        w = c_shp.get_width() if vs3 else 20
        translate(w, 0)
    pop_matrix()
    
    save_frame('###.png')
#     background(0)
#     lights()
#     translate(width /2, height / 2)
#     rotate_x(QUARTER_PI)
#     rotate_y(radians(mouse_x))
#     for i, face in enumerate(m.faces):
#         fill((m.vertices[0][0] * 2) % 255, 200, 200)
#         with begin_closed_shape():
#             vertices([m.vertices[v] for v in face])
#   

