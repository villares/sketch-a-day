"""*
 *        A simple example for class Combination.
 *        fjenett 20090306
 """

add_library('Combinatorics')

def setup():
    size(500, 500)
    background(0)
    fill(255, 0, 0)
    textSize(11)

    chars = "0123456789ABCDEF"
    # Generate the following combinations:
    # place 16 elements on 3 positions
    combinations = Combination(len(chars), 3)
    println(combinations.totalAsInt())
    
    h = height / (combinations.totalAsInt() + 0.5) * 10.8
    x, y, w = 0, h, 48
    while (combinations.hasMore()):
        c = combinations.next()
        t = chars[c[0]] + " " + chars[c[1]] + " " + chars[c[2]]
        text(t, 20 + x, 5 + y)
        x += w
        if x > width:
            x = 0
            y += h
            
    saveFrame("sketch_190518a.png")
    noLoop()
