"""
Draw source code lines with comments in white.
Now with multi0line doctstrings also in white!
"""
import tokenize
from os import path

font_size, line_step, margin = 14, 15, 20

def setup():
    """Load fonts,read code from sketch file and find comments."""
    global sn, src_lines, comments, fr, fb
    size(800, 800)
    fr = create_font("Source Code Pro", font_size)
    fb = create_font("Source Code Pro Bold", font_size)
    sn = path.basename(sketch_path())
    with open(sn+'.py') as f:
        src_lines = f.readlines()
    with open(sn+'.py') as f:  # Open again, to get comments, because…
        comments = [token for toktype, token, start, end_, ln 
                    in tokenize.generate_tokens(f.readline) # …I need f.readline…
                    if toktype == tokenize.COMMENT] # …read tokenize docs about it!
    no_loop()  # makes draw() run once and stop.

def draw():
    """Draw the text."""
    doc_string = None
    for i, ln in enumerate(src_lines, 1):
        fill(0)        # Black
        text_font(fr)  # Regular font
        for comment in comments:
            c_pos = ln.find(comment)
            if c_pos >= 0:    # Comment found
                code = ln[:c_pos]
                c_x = text_width(code)
                text(code, margin, i*line_step)
                fill(255)     # White
                text_font(fb) # Bold
                text(comment, margin+c_x, i*line_step)
                break
        else:  # Lines with no comments (comments loop did not break)
            # Deal with the docstring lines, also in white.
            tq = '"""' # tripple quote
            if ln.strip().startswith(tq) and not doc_string:
                doc_string = i  # Flag line starting with tripple quotes
            if doc_string:
                fill(255)      # White
                text_font(fb)  # Bold
                if doc_string < i and ln.strip().endswith(tq) or ln.count(tq) == 2:
                    doc_string = None  # Turn off flag, ending tripple quote found.
            text(ln, margin, i*line_step) # Draw the line.
    save_frame(sn+'.png')  # now using py5!