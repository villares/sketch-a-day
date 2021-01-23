"""
Draw code lines with comments in white.
Now with multi-line doctstrings also in white!
"""
import tokenize
from os import path

font_size, line_size = 14, 15

def setup():
    """Load fonts, read code from sketch file and find comments."""
    global sn, lines, comments, fr, fb
    size(800, 800)
    fr = createFont("Source Code Pro", font_size)
    fb = createFont("Source Code Pro Bold", font_size)
    sn = path.basename(sketchPath())
    with open(sn + '.pyde') as f:
        lines = f.readlines()
    with open(sn + '.pyde') as f:  # again, to get comments, because...
        comments = [token for toktype, token, start, end_, ln
                    in tokenize.generate_tokens(f.readline)  # read the tokenize docs!
                    if toktype == tokenize.COMMENT]
    noLoop() # draw() runs once and stops
    
def draw():
    """Draw the text."""
    doc_string = None
    for line_y, ln in enumerate(lines, 1):
        fill(0)
        textFont(fr)
        for comm in comments:
            c_pos = ln.find(comm)
            if c_pos >= 0:
                code = ln[:c_pos]
                c_x = textWidth(code)
                text(code, 10, line_y * line_size)
                fill(255)
                textFont(fb)
                text(comm, 10 + c_x , line_y * line_size)
                break
        else: # Lines with no comments (no break on comm in comments loop)
            # Deal with the docstring lines, also in white
            if ln.strip().startswith('"""') and not doc_string:
                doc_string = line_y
            if doc_string:
                fill(255)  
                textFont(fb)         
            if doc_string < line_y and ln.strip().endswith('"""') or ln.count('"""') == 2:
                doc_string = None     
            # Draw the line
            text(ln, 10, line_y * line_size)
    saveFrame(sn + '.png') #genuary2021
