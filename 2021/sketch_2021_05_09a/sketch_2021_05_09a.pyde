drag = None
rgb1 = [32, 32, 32]
rgb2 = [1, 64, 200]

def setup():
    size(1200, 600)
    global bg
    bg = createGraphics(1200, 600)
    beginRecord(bg)
    noStroke()
    background(0)   
    colorMode(RGB)
    for b in range(0, 255, 10):
        for g in range(0, 255, 10):
            for r in range(0, 255, 10):
                fill(r, g, b)
                x, y = pos(r, g, b)
                circle(50 + x, 50 + y, 4)
    colorMode(HSB)
    for b in range(0, 255, 10):
        for h in range(0, 255, 10):
            for s in range(0, 255, 10):
                fill(h, s, b)
                x, y = pos(h, s, b)
                circle(650 + x, 50 + y, 4)
    endRecord()
    
def draw():
    background(bg)
    stroke(255)
    # plot_color(rgb1)
    # plot_color(rgb2)
    for i in range(9):
        t = (i + 1) / 9.0
        c = lerpColor(color(*rgb1), color(*rgb2), t)
        plot_color(as_rgb(c))
    # saveFrame("sketch_2021_05_08a.png")
            
def plot_color(rgb):
    r, g, b = rgb
    c = color(r, g, b)
    fill(c)
    x1, y1 = pos(r, g, b)
    circle(50 + x1, 50 + y1, 10)
    h, s, bri = as_hsb(c)
    x2, y2 = pos(h, s, bri)
    circle(650 + x2, 50 + y2, 10)

def as_rgb(c):
    return red(c), green(c), blue(c)

def as_hsb(c):
    return hue(c), saturation(c), brightness(c)
            
def r_color():
    return color(random(32, 256),
                 random(32, 256),
                 random(32, 256))
    
def pos(a, b, c):
    return b * 1.7 + c * 0.3, a * 1.3 + c * 0.7
