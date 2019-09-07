cols = 2
font_size = 18

def setup():
    global lines
    size(800, 400)
    with open("./sketch_190906a.pyde") as f:
        lines = f.readlines()
    f = createFont("Inconsolata", font_size)
    fb = createFont("Inconsolata-Bold", font_size)
    textFont(f)
    noLoop()
    
def draw():
    # draw code
    line_y = 1
    for ln in lines:
        if ln.strip().startswith("#"):
            fill(255)
        else:
            fill(0)
        text(ln, 10, line_y * font_size)
        line_y += 1
        
    
