import py5

def setup():
    global pg, mascara, surface
    py5.size(800, 800)
    pg = py5.create_graphics(py5.width, py5.height)
    mascara = py5.create_graphics(py5.height, py5.height)
    mascara.begin_draw()
    for x in range(20, 800, 195):
        for y in range(20, 800, 195):     
            mascara.rect(x, y, 175, 175, 10)
    mascara.end_draw()

def draw():
    py5.background(255)
    f = py5.frame_count
    s = py5.sin(py5.radians(f * 2))
    d = 300 + 200 * s
    x = py5.lerp(300 - 195, 300 + 195, (1 + s) / 2)
    y = py5.remap(f, 1, 180, -25, py5.height + 25) 
    pg.begin_draw()
    pg.background(0, 100, 0)
    pg.fill(0, 0, 100)
    pg.circle(300, 300, d)
    pg.circle(600 + 175 / 2, y, 50)
    pg.circle(x, 600 + 175 / 2, 50)
    pg.end_draw()
    pg.mask(mascara)
    py5.image(pg, 0, 0)
    
    if f <= 180 and f % 2:
        py5.save_frame('###.png')
    elif f == 181:
        py5.exit_sketch()

py5.run_sketch()