import py5

S = 2  # scale factor

def setup():
    global osb, svg, mask
    py5.size(500, 500)
    w, h = 500 * S, 500 * S
    osb = py5.create_graphics(w, h)
    mask = py5.create_graphics(w, h)
    mask.begin_draw()
    mask.no_stroke()
    mask.circle(w / 2, h / 2, w)
    mask.end_draw()
    osb.begin_draw()
    osb.background(py5.color(0))
    osb.scale(S)
    for x in range(0, py5.width, 10):
        osb.stroke('white')
        osb.line(x, 0, x, py5.height)
    osb.end_draw()
    osb.mask(mask)
    py5.image(osb, 0, 0, py5.width, py5.height)
    osb.save('out.png', drop_alpha=False)

py5.run_sketch(block=False)
