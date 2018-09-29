
def setup():
    size(100, 100)
    fill(0)
    textSize(60)
    textAlign(CENTER, CENTER)
    for c in range(10, 256):
        gliph = chr(c)
        if gliph != u"":
            background(255)
            text(gliph, width/2, height/2)
            tally = count_pixels()
            print("{}({}) black: {} white: {} other: {}"
              .format(c, gliph, *tally))


def count_pixels():
    black, white, other = 0, 0, 0
    for x in range(width):
        for y in range(height):
            pix = get(x, y)
            if pix == color(0):
                black += 1
            elif pix == color(255):
                white += 1
            else:
                other += 1
    return black, white, other
            
            
