from random import choice

def setup():
    global chrs
    size(640, 480)
    img = loadImage("ZX81_characters_0x00-3F,_0x80-BF.png")
    chrs = [img.get(x * 16, y * 16, 16, 16) 
            for x in range(16)
            for y in range(8)]
    frameRate(4)
    
def draw():
    for x in range(0, width, 16):
        for y in range(0, height, 16):
            image(choice(chrs), x, y)
