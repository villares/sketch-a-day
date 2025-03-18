# this is a py5 "imported mode" sketch, you'll need the py5 runner tool
# learn more at https://py5coding.org

def setup():
    size(800, 800)
    rect_mode(CENTER)
    background(0)
    no_stroke()
    rows = cols = 20
    siz = width / cols
    for row in range(rows):  # 0, 1, 2 ... rows - 1
        y = row * siz + siz / 2
        for col in range(cols):  # 0, 1, 2, ... cols - 1
            x = col * siz + siz / 2
            w = random(10, siz)
            h = random(10, siz)
            fill(w * 5, h * 5, 128)
            rect(x, y, w, h)
    save('out.png')