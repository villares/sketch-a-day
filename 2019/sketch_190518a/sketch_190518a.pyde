"""
Port and tweak of a simple example for class Combination.
by fjenett 20090306
"""

add_library('Combinatorics')

def setup():
    size(500, 500)
    background(0)
    colorMode(HSB)
    chars, n = "0123456789ABCDEF", 3
    # chars, n = "0123456789", 3
    # Generate the following combinations:
    # place 16 elements on 3 positions
    combinations = Combination(len(chars), n)
    println(combinations.totalAsInt())

    h = height / (combinations.totalAsInt() + 0.5) * 9.6
    x, y, w = 0, 0, (width - 20) / 10
    textSize(10)
    i = 0
    while combinations.hasMore():
        combination = combinations.next()
        txt = ""
        for n in combination:
            elem = chars[n]
            txt += elem
        m = (int(txt, 16))
        fill(m / 16 , 255, 255)
        text(txt, 20 + x, 20 + y * h)
        x += w
        if x > width - 50:
            x = 0
            y += 1
            print y
        i += 1
        # print i

    saveFrame("sketch_190518a.png")
    noLoop()
