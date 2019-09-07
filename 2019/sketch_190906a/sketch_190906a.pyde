import tokenize

cols = 2
font_size = 18

def setup():
    global lines
    size(600, 600)
    with open("./sketch_190906a.pyde") as f:
        lines = f.readlines()
    f = createFont("Inconsolata", font_size)
    fb = createFont("Inconsolata-Bold", font_size)
    textFont(f)
    noLoop() # draw() runs once and stops
    
def draw():
    line_y = 1
    for ln in lines:
        comment_pos = ln.find("#")
        quote =  ln.find("'") < comment_pos and \
                 ln.find('"') < comment_pos
        print(comment_pos)
        if comment_pos >= 0 and quote:
            code = ln[:comment_pos]
            comment = ln[comment_pos:]
            comment_x = textWidth(code)
            fill(0)
            text(code, 10, line_y * font_size)
            fill(255)
            text(comment, 10 + comment_x, line_y * font_size)
        else:
            fill(0)
            text(ln, 10, line_y * font_size)
        line_y += 1
        
    
