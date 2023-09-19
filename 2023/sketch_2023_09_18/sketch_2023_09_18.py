from pathlib import Path
import py5

files = []
line_h = 200
col_width = 200

def setup():
    py5.size(1000, 1000)
    py5.text_align(py5.LEFT, py5.TOP)
   # py5.select_folder('Select a folder', list_files)

def draw():
    i = 0
    x = y = 0
    while i < len(files) and x < py5.width:
        py5.fill(255)
        py5.rect(x, y, col_width - 2, line_h - 2)
        py5.fill(0)
        py5.text(files[i][0], x, y)
        y += line_h
        if y > py5.height:
            y = 0
            x += col_width


def list_files(folder):
    files.clear()
    if folder:
        for f in Path(folder).iterdir():
            files.append((f.name, f))

def key_pressed():
    if py5.key == 'o':
        py5.select_folder('Select a folder', list_files)


py5.run_sketch(block=False)

