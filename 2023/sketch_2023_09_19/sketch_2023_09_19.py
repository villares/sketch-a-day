from pathlib import Path

import py5
import imageio

BACKGROUND = py5.color(200, 200, 240)
SELECTED = py5.color(100, 100, 200)

files = []
line_h = 160
coll_w = 160
start = 0
over = None

def setup():
    py5.size(800, 800)
    py5.text_align(py5.LEFT, py5.TOP)
    list_files(Path.cwd().parent.parent)

def draw():
    global over
    over = None
    py5.background(BACKGROUND)
    i = start
    x = y = 0
    while i < len(files) and x < py5.width:
        name, _, _, img = files[i]
        if mouse_over(x, y):
            py5.fill(SELECTED)
            files[i][2] = True
        else:
            py5.fill(255)
            files[i][2] = False
        if img:
            py5.image(img, x + 1, y + 1, coll_w - 2, line_h - 2)
        else:
            py5.rect(x + 1, y + 1, coll_w - 2, line_h - 2)
        py5.fill(0)
        py5.text(name, x, y)
        y += line_h
        if y > py5.height:
            y = 0
            x += coll_w
        i += 1

def mouse_over(x, y):
    return x < py5.mouse_x < x + coll_w and y < py5.mouse_y < y + line_h

def list_files(folder):
    parent = folder.parent
    files.append([parent.name[:30], parent, None, None])
    if folder:
        for f in Path(folder).iterdir():
            files.append([f.name[:30], f, None, None])
    for i, (_, f, _, _) in enumerate(files):
        if valid_image(f):
            files[i][3] = py5.load_image(f)

def mouse_pressed():
    for f in files:
        if f[2] and f[1].is_dir():
            print(f)

            files.clear()
            list_files(f[1])        

def valid_image(path):
    if not path.is_file():
        return False
    elif path.suffix.lower() in ('.svg', '.png', '.jpg', '.jpeg', '.gif', '.tif'):
        return True
    else:
        try:
            imageio.v3.imread(path)
            return True
        except:
            return False

def key_pressed():
    if py5.key == 'o':
        files.clear()
        py5.select_folder('Select a folder', list_files)


py5.run_sketch(block=False)

