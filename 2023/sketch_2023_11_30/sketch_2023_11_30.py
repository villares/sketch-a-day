# Using numpy to order glyphs by black pixel count

import py5
import numpy as np

glyphs = '#1234567890.XZ*'
W = 60

def setup():
    py5.size(900, 120)
    f = py5.create_font('Inconsolata Black', 60)
    pg = py5.create_graphics(W, W)  # an offscreen buffer
    pg.no_smooth()  # to disable antialiasing, it must be done before begin_draw()
    pg.begin_draw()
    pg.text_size(W)
    pg.fill(0)
    pg.text_font(f)
    pg.text_align(py5.CENTER, py5.CENTER)
    pg.end_draw()
    counts = []
    for glyph in glyphs:
        pg.begin_draw()
        pg.background(255)
        pg.text(glyph, W / 2, W / 2 - 2)
        pg.load_np_pixels()
        pxs = pg.np_pixels
        black = [255, 0, 0, 0]  # Alpha, R, G, B
        black_count = np.count_nonzero(np.all(pxs==black, axis=2))
        pg.end_draw()
        py5.image(pg, 0, 0)
        py5.translate(W, 0)
        counts.append((black_count, glyph, pg.copy()))
    counts.sort()
    py5.reset_matrix()
    py5.tint(200, 200, 0)
    for count, glyph, img in counts:
        py5.image(img, 0, W)
        #py5.text_font(f)
        #py5.text_align(py5.CENTER, py5.CENTER)
        #py5.text(glyph, W / 2, W / 2 - 2 + W)
        py5.translate(W, 0)
        
py5.run_sketch()
