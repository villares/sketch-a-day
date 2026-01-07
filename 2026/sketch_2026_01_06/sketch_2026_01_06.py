import pickle

import py5
import py5_tools

import glyphs

def setup():
    global gs
    py5.size(800, 800)
    with open("glyphs.pickle", 'rb') as f:
        gs = pickle.load(f)
        print('glyphs loaded')
    py5_tools.animated_gif(
        'out2.gif',
        frame_numbers=range(1, 361, 5),
        duration=0.16
   )

def draw():
    f = py5.frame_count

    if f > 180:
        py5.color_mode(py5.CMAP, 'viridis', 255)
    else:
        py5.color_mode(py5.CMAP, 'viridis_r', 255)
    py5.background(0)
    py5.no_fill() 
    py5.stroke_join(py5.ROUND)
    glyphs.Glyph.module_size = 18
    sizes = []
    for y in range(10, 50, 10):
        x = 3
        for i, letter in enumerate('genuary'):
            # maybe I should use x instead of i here...
            w = 10 + 9 * py5.sin(py5.radians(y + i * 10 + f))
            py5.stroke_weight(w)
            py5.stroke(y * 5)
            glyph = gs[letter]
            glyph.plot(x, y)
            x += glyph.width
    
py5.run_sketch(block=False)

