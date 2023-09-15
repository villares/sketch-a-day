import py5

def setup():
    global pg, tam_quad
    py5.size(800, 800)
    tam_quad = 175
    pg = py5.create_graphics(tam_quad, tam_quad)

def draw():
    py5.background(255)
    f = py5.frame_count
    step = py5.TWO_PI / 16
    i = 0
    for y in range(20, 800, 195):
        for x in range(20, 800, 195):         
            s = py5.cos(py5.radians(f * 2) + i * step)
            d = 55 + 50 * s
            yc = py5.remap(s, -1, 1, 0, tam_quad)
            pg.begin_draw()
            pg.background(100, 200, 0)
            pg.fill(0, 0, 200)
            pg.circle(175 / 2, yc, d)
            pg.end_draw()
            py5.image(pg, x, y)
            i += 1
#     if f <= 180 and f % 2:
#         py5.save_frame('###.png')
#     elif f == 181:
#         py5.exit_sketch()

py5.run_sketch()