import os
import io
import PIL.Image
import py5
import difflib
import tkinter 


current = 0
code = previous_code = ''
font_size, line_step, margin = 12, 12, 20

def select_folder():
    global image_paths
    #file = tkinter.filedialog.askopenfilename()
    folder = tkinter.filedialog.askdirectory()
    try:
        file_list = sorted(os.listdir(folder))  # get list of files in folder
    except:
        file_list = []
    image_paths = [os.path.join(folder, f) for f in file_list
                   if os.path.isfile(os.path.join(folder, f))
                   and f.lower().endswith(('.png', '.jpg', 'jpeg',
                                      '.tiff', '.bmp', '.gif'))]



def setup():
    global fr, fb
    py5.size(1600, 1000)
    select_folder()
    walk_images(0)
    fr = py5.create_font("Source Code Pro", font_size)
    fb = py5.create_font("Source Code Pro Bold", font_size)



def draw():
    py5.background(240)
    py5.image(img, 50, 50)
    draw_code()
    py5.fill(0)
    py5.text(image_paths[current], 50, 30)
#     py5.save(f'{current}.png')
#     walk_images(1)
#     if current == 0:
#         py5.exit_sketch()

def key_pressed():
    if py5.key == py5.ESC:
        py5.exit_sketch()
    elif py5.key_code == py5.DOWN:
        walk_images(1)
    elif py5.key_code == py5.UP:
        walk_images(-1)


def walk_images(i):
    global current, img, code, previous_code
    if len(image_paths) == 0:
        return
    current = (current + i) % len(image_paths)
    img, info = load_image_and_data(current)
    previous_code = code
    code = info.get('code', '').replace('    \n', '\n').replace('\n\n\n', '')

def load_image_and_data(i, resize=None):
    img = PIL.Image.open(image_paths[i])
    cur_width, cur_height = img.size
    if resize:
        new_width, new_height = resize
        scale = min(new_height / cur_height, new_width / cur_width)
        img = img.resize(
            (int(cur_width * scale), int(cur_height * scale)),
            PIL.Image.Resampling.LANCZOS,
        )
    return py5.convert_image(img), img.info

def draw_code():
    with py5.push():
        py5.text_font(fb)
        differ = difflib.Differ()
        colors = {' ': 0, '-': 0xFFFF0000, '+': 0xFF0000FF, '?': 0xFF00CC00}
        for li in differ.compare(previous_code.splitlines(), code.splitlines()):
            py5.fill(colors[li[0]])
            py5.text(li, 1000, 50)
            py5.translate(0, line_step)
    
    
#     py5.fill(255, 0, 0)
#     py5.text(previous_code, 1000, 100)
#     py5.fill(0)    
#     py5.text(code, 1000, 100)
#     for l in t:
#         print(l)

py5.run_sketch()


'''
with io.StringIO(code) as c:
        tokens = [(toktype, token) for toktype, token, start, end_, ln
                  in tokenize.generate_tokens(c.readline)]  # read the
    for toty, to in tokens:
        space = ' ' if toty not in (54, 4, 5) else ''
        print(f'{to}{space}', end='')
        
    ###########
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
    for i, ln in enumerate(lines, 1):
        fill(0)
        textFont(fr)
        for comment in comments:
            c_pos = ln.find(comment)
            if c_pos >= 0:
                code = ln[:c_pos]
                c_x = textWidth(code)
                text(code, margin, i * line_step)
                fill(255)
                textFont(fb)
                text(comment, margin + c_x , i * line_step)
                break
        else: # Lines with no comments (no break on comm in comments loop)
            # Deal with the docstring lines, also in white
            if ln.strip().startswith('"""') and not doc_string:
                doc_string = i
            if doc_string:
                fill(255)  
                textFont(fb)         
            if doc_string < i and ln.strip().endswith('"""') or ln.count('"""') == 2:
                doc_string = None     
            # Draw the line
            text(ln, margin, i * line_step)
    saveFrame(sn + '.png') #genuary2021
'''