import py5

step = 10

def setup():
    global osb, fl
    py5.size(800, 600, py5.P2D)
    w, h = py5.width, py5.height
    fl = py5.load_shape('Fleur-de-lis-fill.svg')
    fl.disable_style()
    py5.shape_mode(py5.CENTER)
    f = py5.create_font('Tomorrow Bold', 180)
    osb = py5.create_graphics(w, h)
    osb.begin_draw()
    osb.text_font(f)
    osb.text_align(3, 3) # CENTER, CENTER
    osb.text_leading(180)
#     for t in range(255, 150, -10):
#         osb.text_size(t)
#         osb.text_leading(t)
#         osb.fill(150 + 255 - t)
    osb.text('FELIZ\nNATAL', w / 2, h / 2)
    osb.end_draw()

def draw():
    py5.background(255, 128, 0)
    py5.fill(0, 0, 250)
    py5.no_stroke()
    py5.shape(fl, 400, 300, 600, 600)
    py5.stroke_weight(4)
    py5.stroke(0, 100, 0)
    for n in range(0, 900, step):
        wave(0, n, py5.width, n, [py5.brightness(osb.get_pixels(x, n))
                                  for x in range(0, py5.width, step)],
            py5.sin(py5.frame_count / 3) / 15
        )
        wave(n, 0, n, py5.height,
                [py5.brightness(osb.get_pixels(n, y))
                 for y in range(0, py5.height, step)],
                py5.sin(py5.frame_count / 3) / 15
             )
    if py5.frame_count / 3 < py5.TWO_PI:
        py5.save_frame('###.png')

def key_pressed():
    py5.save(__file__[:-2] + f'{py5.frame_count}.png')

def wave(x1, y1, x2, y2, samples, offset):
    """
    dois pares (x, y), largura, número de ondas
    """
    L = py5.dist(x1, y1, x2, y2)
    n = len(samples)
    py5.no_fill()
    with py5.push_matrix():
        py5.translate(x1, y1)
        angle = py5.atan2(x1 - x2, y2 - y1)
        py5.rotate(angle)
        dy = L / (n + 2) 
        point_L = []
        point_L.append((0, 0))
        with py5.begin_shape():
            py5.vertex(0, 0)
            for i in range(1, n + 1):
                s = 1 + samples[i-1] * offset
                point_L.append((0, i * dy, 0))
                if i % 2:
                    point_L.append((-s, i * dy + dy / 2.0, s))
                    point_L.append((0, i * dy + dy, s))
                else:
                    point_L.append((s, i * dy + dy / 2.0, s))
                    point_L.append((0, i * dy + dy, s))
            point_L.append((0, L, 0))
            for p1, p2 in zip(
                          point_L[1:-1],
                          point_L[2:],
                          ):
                p1x, p1y, s = p1
                p2x, p2y, _ = p2
                m12x, m12y = (p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2
                if p2 == (0, L):
                    py5.quadratic_vertex(p1x, p1y, p2x, p2y)
                else:
                    py5.quadratic_vertex(p1x, p1y, m12x, m12y)

py5.run_sketch()