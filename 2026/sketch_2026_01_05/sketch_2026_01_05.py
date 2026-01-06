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
    # global glyph # used for debugging
    f = py5.frame_count
    py5.background(0)
    py5.no_fill() 
    py5.stroke(255)
    py5.stroke_join(py5.ROUND)
    glyphs.Glyph.module_size = 18
    x, y = 3, 25  # in glyph module grid units
    sizes = []
    for i, letter in enumerate('genuary'):
        # maybe I should use x instead of i here...
        w = 10 + 9 * py5.sin(py5.radians(i * 10 + f))
        py5.stroke_weight(w)
        glyph = gs[letter]
        glyph.plot(x, y)
        x += glyph.width
    
py5.run_sketch(block=False)

