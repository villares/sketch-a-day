def setup():
    size(1200, 600)
    noStroke()
    background(0)   
    colorMode(RGB)
    for b in range(0, 255, 10):
        for g in range(0, 255, 10):
            for r in range(0, 255, 10):
                fill(r, g, b)
                x = 50 + g * 1.7 + b * 0.3
                y = 50 + r * 1.3 + b * 0.7
                circle(x, y, 4)
    colorMode(HSB)
    for b in range(0, 255, 10):
        for h in range(0, 255, 10):
            for s in range(0, 255, 10):
                fill(h, s, b)
                x = 650 + s * 1.7 + b * 0.3
                y = 50 + h * 1.3 + b * 0.7
                circle(x, y, 4)
    # saveFrame("sketch_2021_05_07a.png")
                
