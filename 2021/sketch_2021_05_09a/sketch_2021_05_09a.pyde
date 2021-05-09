hsb_mode = True
rgb1 = [200, 50, 200]
rgb2 = [50, 200, 200]

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
    textAlign(CENTER)
    textSize(20)
    
def draw():
    background(bg)
    stroke(255)
    colorMode(RGB)
    c1 = color(*rgb1)
    plot_color(c1)
    c2 =  color(*rgb2)
    plot_color(c2)
    fill(255)
    if hsb_mode:
        colorMode(HSB)
        text("HSB mode", width / 2, 30)
    else:
        colorMode(RGB)
        text("RGB mode", width / 2, 30)
    
    for i in range(10):
        t = (i + 1) / 9.0
        c3 = lerpColor(c1, c2, t)
        plot_color(c3)
            
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


def mouseDragged():
    if mouseButton == LEFT:
        rgb1[1] = (-50 + mouseX - rgb1[2] * 0.3) / 1.7
        rgb1[0] = (-50 + mouseY - rgb1[2] * 0.7) / 1.3
    else:
        rgb2[1] = (-50 + mouseX - rgb2[2] * 0.3) / 1.7
        rgb2[0] = (-50 + mouseY - rgb2[2] * 0.7) / 1.3
    

def keyPressed():
    global hsb_mode
    hsb_mode = not hsb_mode
