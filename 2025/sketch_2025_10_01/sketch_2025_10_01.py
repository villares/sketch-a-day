# this is a py5 "imported mode" sketch, you'll need the py5 runner tool
# learn more at https://py5coding.org

def setup():
    size(1600, 800)
    rect_mode(CENTER)
    background(0)
    no_stroke()
    rows = 25
    cols = 50
    siz = width / cols
    for row in range(rows):  # 0, 1, 2 ... rows - 1
        y = row * siz + siz / 2
        for col in range(cols):  # 0, 1, 2, ... cols - 1
            x = col * siz + siz / 2
            w = siz / 2 + siz / 3 * cos(x / 150)
            h = siz / 2 + siz / 3 * sin(y / 150)
            fill(w * 5, h * 5, 128)
            rect(x, y, w, h)
            w = siz / 2 + siz / 3 * sin(x / 150) 
            h = siz / 2 + siz / 3 * cos(y / 150)
            fill(w * 5, h * 5, 128)
            rect(x, y, w, h)
            
    save('out.png')
