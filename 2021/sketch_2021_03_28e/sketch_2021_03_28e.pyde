def setup():
    size(650, 650)
    
def draw():
    background(0)
    total_h = 0
    while total_h < 600:
        total_w = 0
        nh = noise(total_w * 0.005,
                  total_h * 0.005,
                  frameCount * 0.001)
        true_h = h = 36 * nh
        if total_h + h > 600:
                h = 600 - total_h
        while total_w < 600:
            nw = noise(total_w * 0.005, 
                      total_h * 0.005,
                      frameCount * 0.001)
            w = 36 * nw
            fill(0, w * 8, true_h * 8)
            if total_w + w > 600:
                w = 600 - total_w
            rect(25 + total_w,
                25 + total_h, w, h)
            total_w += w
        total_h += h
