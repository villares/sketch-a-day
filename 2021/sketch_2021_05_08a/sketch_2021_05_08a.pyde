def setup():
    size(1200, 600)
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
    stroke(255)
    c1 = r_color()
    plot_color(c1)
    c2 = r_color()
    plot_color(c2)
    for i in range(10):
        t = (i + 1) / 9.0
        c3 = lerpColor(c1, c2, t)
        plot_color(c3)
    saveFrame("sketch_2021_05_08a.png")
            
def plot_color(c):
    fill(c)
    r, g, b = as_rgb(c)
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
