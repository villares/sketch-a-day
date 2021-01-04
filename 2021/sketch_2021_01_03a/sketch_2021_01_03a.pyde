"""
sketch_2021_01_03 #genuary2021 #genuary #generative #creativeCoding 
#Processing #Python #UNICODE Prompt was: Something Human.
I think my friend Luciano Ramalho @ramalhoorg puts it in more elegant terms,
but the feeling is: Unicode is one of the great human achievements.
"""

import unicodedata

i = 0

def setup():
    global w, unicode_glyphs
    size(512, 512)
    frameRate(10)
    w = width / 32
    unicode_glyphs = u''.join(
        unichr(c)
        for c in xrange(1024 * 16) # not 0x10ffff + 1
        if unicodedata.category(unichr(c))[0] in 'LMNPSZ'
        ) 
       
def draw():
    global i
    background(0)   
    for x in range(32):
        for y in range(32):
            text(unicode_glyphs[i], x * w, w + y * w)
            i = (i + 1) % len(unicode_glyphs)
