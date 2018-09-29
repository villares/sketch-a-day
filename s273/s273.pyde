table = []

def setup():
    global gliphs, tally
    size(100, 200)
    background(255)
    fill(0)
    noSmooth() # turns off antialiasing
    textAlign(CENTER, CENTER)
    printable_ascii = list(range(32, 127)) + list(range(161, 256))
    for c in printable_ascii:
        gliph = chr(c)
        background(255)
        text(gliph, width/2, height/2)
        b, w, o = count_pixels()
        print("{}({}) black: {} white: {} other: {}"
              .format(c, gliph, b, w, o))
        table.append((gliph, b, w, o))
    table.sort(key=lambda s: s[1])
    gliphs = "".join([gliph for gliph, b, w, o in table])
    print(gliphs)

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
            
def draw():
    background(255)
    i = int(map(mouseY, 0, height-1, 0, len(gliphs)-1))
    gliph, b, w, o = table[i]
    textSize(8)
    text("B:{}\nW:{}:\nO:{}".format(b, w, o), width/2, 20)
    textSize(100)
    text(gliph, width/2, height/2)
