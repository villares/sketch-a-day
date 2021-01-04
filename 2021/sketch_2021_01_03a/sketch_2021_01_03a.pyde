"""
sketch_2021_01_03 #genuary2021 #genuary #generative #creativeCoding 
Prompt was Something Human, I think my friend Ramalho puts it in more
elegant terms, but Unicode is one of the great human achievemnts.
"""

import unicodedata

i = 0

def setup():
    global w, unicode_glyphs
    size(512, 512)
    w = width / 32
    unicode_glyphs = u''.join(
        unichr(char)
        for char in xrange(1024 * 16) # 0x10ffff + 1
        if unicodedata.category(unichr(char))[0] in ('LMNPSZ')
        ) 
       
def draw():
    global i
    background(0)
   
    for x in range(32):
        for y in range(32):
            text(unicode_glyphs[i], x * w, y * w)
            i = (i + 1) % len(unicode_glyphs)

    # print unicode_glyphs
    # noLoop()
