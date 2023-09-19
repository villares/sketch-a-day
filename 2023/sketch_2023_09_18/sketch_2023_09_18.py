from pathlib import Path
import py5

BACKGROUND = py5.color(200, 200, 240)
SELECTED = py5.color(100, 100, 200)

files = []
line_h = 160
coll_w = 160
start = 0

def setup():
    py5.size(800, 800)
    py5.text_align(py5.LEFT, py5.TOP)
    list_files(Path.cwd().parent.parent)

def draw():
    py5.background(BACKGROUND)
    i = start
    x = y = 0
    while i < len(files) and x < py5.width:
        py5.fill(SELECTED if mouse_over(x, y) else 255)
        py5.rect(x + 1, y + 1, coll_w - 2, line_h - 2)
        py5.fill(0)
        py5.text(files[i][0], x, y)
        y += line_h
        if y > py5.height:
            y = 0
            x += coll_w
        i += 1

def mouse_over(x, y):
    return x < py5.mouse_x < x + coll_w and y < py5.mouse_y < y + line_h

def list_files(folder):
    if folder:
        for f in Path(folder).iterdir():
            files.append([f.name[:16], f, None, None])

def key_pressed():
    if py5.key == 'o':
        files.clear()
        py5.select_folder('Select a folder', list_files)


py5.run_sketch(block=False)

