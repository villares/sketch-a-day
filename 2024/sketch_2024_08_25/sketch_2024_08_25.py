import random

import py5
import ziaplot as zp

TMP = 'tmp.svg'

def setup():
    py5.size(600, 400)
    py5.window_title('Ziaplot in py5')
    py5.no_loop()
    
def draw():
    py5.background(240)
    makedata()
    img = py5.convert_image(TMP)
    py5.image(img, 50, 75, 500, 300)
    py5.fill(0)
    py5.text_size(25)
    py5.text_align(py5.CENTER)
    py5.text('click to get a new one', py5.width / 2, 50)

def mouse_pressed():
    py5.redraw()

def makedata():
        ''' Generate some randomized data and plot it, then
            save a temporary SVG file. '''
        n = 15
        y = [(i*2) + random.normalvariate(10, 2) for i in range(n)]
        avg = sum(y)/len(y)
        x = list(range(n))
        p = zp.Graph()
        p += zp.PolyLine(x, y).marker('o')
        p += zp.HLine(avg)
        #return p.imagebytes()
        p.save(TMP)

py5.run_sketch()
