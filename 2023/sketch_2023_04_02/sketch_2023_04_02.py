margin = 20

def setup():
    size(1800, 600)
    text_align(LEFT, CENTER)
    background(128)
    no_stroke()
    for n in (3, 4, 5):
        grid(margin, margin, height - margin * 2, n)
        translate(600, 0)
    save('out.png')

def grid(xo, yo, largura_total, n=5):
    w = largura_total / n
    color_step = 255 / n
    half_step = color_step / 2
    text_size(w / 8)
    text_leading(w / 9)
    for j in range(n):
        x = xo + w * j + w / 2
        for i in range(n):
            y = yo + w * i + w / 2
            B = round(half_step + i * color_step)
            G = round(half_step + j * color_step)      
            R = round(-half_step + 255 - i * color_step)
            fill(R, G, B) 
            circle(x, y, w * 0.98)
            fill(255)
            text(f'R:{R}\nG:{G}\nB:{B}\n', x, y) 
            
