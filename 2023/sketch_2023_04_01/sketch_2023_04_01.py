margin = 60

def setup():
    size(800, 800)
    text_align(LEFT, CENTER)
    text_size(20)
    text_leading(19)
    background(0)
    grid(margin, margin, width - margin * 2)
    save('out.png')

def grid(xo, yo, largura_total, n=4):
    w = largura_total / n
    color_step = 255 / (n - 1)
    for j in range(n):
        x = xo + w * j + w / 2
        for i in range(n):
            y = yo + w * i + w / 2
            R = i * color_step
            G = j * color_step        
            B = 255 - i * color_step
            fill(R, G, B) 
            circle(x, y, w * 0.98)
            fill(0)
            text(f'R: {R:.1f}\nG: {G:.1f}\nB: {B:.1f}\n', x, y) 
            
