""" Draw code with comments in white """
import tokenize

font_size = 18

def setup():
    global lines, comments, fr, fb
    size(800, 800)
    with open("./sketch_190906a.pyde") as f:
        lines = f.readlines()
    comments = [] # list of comments
    with open("./sketch_190906a.pyde") as f:
      for tokens in tokenize.generate_tokens(f.readline):
          toktype, tok, start, end_, ln = tokens
          if toktype == tokenize.COMMENT:
            comments.append(tok)
    fr = createFont("Inconsolata", font_size)
    fb = createFont("Inconsolata-Bold", font_size)
    noLoop() # draw() runs once and stops
    
def draw():
    line_y = 1
    for ln in lines:
        for comm in comments:
            c_pos = ln.find(comm)
            fill(0)
            textFont(fr)
            if c_pos >= 0:
                code = ln[:c_pos]
                c_x = textWidth(code)
                text(code, 10, line_y * font_size)
                fill(255)
                textFont(fb)
                text(comm, 10 + c_x , line_y * font_size)
                break
        else: # no comments (no break on comm in comments loop)
            if ln.strip().startswith('"""'): # get the docstrings
                fill(255)  
                textFont(fb)              
            text(ln, 10, line_y * font_size)
        line_y += 1
    
