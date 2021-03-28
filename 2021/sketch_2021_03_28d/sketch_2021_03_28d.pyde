def setup():
    size(650, 650)
    background(0)
    colorMode(HSB)
    total_h = 0
    while total_h < 600:
        total_w = 0
        h = int(random(1, 33))
        if total_h + h <= 600:
            while total_w < 600:
                w = int(random(1, 33))
                if total_w + w <= 600:
                    fill(w * 8, 200, h * 8)
                    rect(25 + total_w,
                        25 + total_h, w, h)
                    total_w += w
            total_h += h
            
