import py5

S = 10  # scale factor

def setup():
    global osb, svg, mask
    py5.size(500, 500)
    py5.color_mode(py5.CMAP, py5.mpl_cmaps.VIRIDIS_R, 255)
    w, h = 500 * S, 500 * S
    osb = py5.create_graphics(w, h)
    py5.no_loop()
    
    svg = py5.load_shape('Aiga_departingflights.svg')
    svg.disable_style()
    mask = py5.create_graphics(w, h)
    mask.begin_draw()
    mask.no_stroke()
    mask.shape(svg, w * 0.05, h * 0.05, w * 0.9, h * 0.9)
    mask.end_draw()
    osb.no_smooth()  # before begin_draw!
    osb.begin_draw()
    osb.stroke_cap(py5.SQUARE)
    osb.background(py5.color(0))
    osb.scale(S)
    for _ in range(200):
        x = py5.random_int(-255, 500 + 255)
        y = py5.random_int(-255, 500 + 255)
        for i in range(255):
            if py5.random_int(1, 10) > 5:
                # you need to use py5.color() with Py5Graphics attributes
                osb.stroke(py5.color(i))    
            else:
                osb.stroke(0, 0)    
            osb.line(x + i, y, x + i, y + 255)
    osb.end_draw()
    osb.mask(mask)
    py5.background('black')
    py5.image(osb, 0, 0, py5.width, py5.height)
    osb.save('out.png', drop_alpha=False)  # necessary for the masking!


py5.run_sketch(block=False)
