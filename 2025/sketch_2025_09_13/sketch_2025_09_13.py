import py5

def setup():
    global osb
    py5.size(500, 500)
    py5.color_mode(py5.CMAP, py5.mpl_cmaps.VIRIDIS_R, 255)
    osb = py5.create_graphics(500, 500)
    
def draw():
    osb.begin_draw()
    osb.background(0)
    for y in range(-100, 600, 10):
        x = py5.random_int(-128, 500 + 128)
        for i in range(255):
            if py5.random_int(1, 10) > 5:
                c = i
            else:
                c = float('NaN')
            # you need to use py5.color() with Py5Graphics attributes
            osb.stroke(py5.color(c))    
            osb.line(x + i, y, x + i, y + 100)
    osb.end_draw()
    py5.image(osb, 0, 0)
    if 0 < py5.frame_count <= 10:
        py5.save_frame('##.png')
    
py5.run_sketch(block=False)
