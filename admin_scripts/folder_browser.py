#!/home/villares/thonny-python-env/bin/python3

"""
A naive image browser experiment.

Images with thick borders are clickable folders.
(it displays images from inside the subfolders)
Left-click to navigate folders.
Right-click to open files/folders with OS.

SHIFT/CONTROL + click to select/desselect items.

's' to toggle sort by name or by file extension
'm' to toggle modes

TODO:
   -[ ] Make the preview mode
   -[ ] Make a diff modw
   -[X] Create a "selected items list" feature
       - Currently saves selection in
         folder_browser_selection.txt
         whic can be used by folder_diff.py

"""
import sys
import subprocess
from pathlib import Path
from zipfile import ZipFile
from functools import lru_cache

import py5
import PIL.Image

ICONS_ZIP = Path(__file__).parent / 'folder_browser_icons.zip'
SELECTION = Path(__file__).parent / 'folder_browser_selection.txt'
BACKGROUND = py5.color(128, 128, 150)
CLICKABLE = py5.color(0, 0, 255)
OVER = py5.color(255)
SELECTED_FILL = py5.color(255, 64)
DEBUG = False

if DEBUG:
    print(f'Running on: {sys.executable}')

line_h = 150
margin = 12
image_h = line_h - margin * 2
coll_w = 150

mode = {
 'mode': 'browse',
 'sort_by': 'name',
}

scroll = {
    'start': 0,
    'end': 0,
    'first_row': 0,
    'previous_row': [0],
    'last_scroll': [],
    'selection': [],
    }

hidden_files = False
files = []

def setup():
    py5.size(800, 800)
    py5.text_align(py5.LEFT, py5.TOP)
    py5.window_resizable(True)
    load_icon_imgs()
    update_files(Path.cwd())


def draw():
    py5.background(BACKGROUND)        
    if mode['mode'] != 'diff':
        draw_browser()        
    
def draw_browser():
    global over, max_width
    over = None
    if mode['mode'] == 'browse':
        max_width = py5.width
        max_height = py5.height
    if mode['mode'] == 'browse_preview':
        max_width = py5.width - py5.height
        max_height = py5.height    
    i = scroll['start']
    x = 0
    y = margin
    first_row = True
    while i < len(files):
        rw = rh = coll_w - margin * 2
        name, fp, is_valid_img = files[i]
        if len(name) > 25:
            name = name[:15] + '…' + name[-8:]
        thumb = None
        # skipping first element, get thumb dims, if possible
        if i != 0 and (thumb := get_picture(fp)):
            w, h = thumb.width, thumb.height
            ratio = w / h
            rw, rh = image_h * ratio, image_h
            if rw > max_width - margin * 2:
                rw = max_width - margin * 2
                rh = rw / ratio
        # move to next row and record first row length    
        if x > max_width - rw - margin :
            x = 0
            y += line_h
            if first_row:
                scroll['first_row'] = i - scroll['start']
                first_row = False
        # stop if position outside screen        
        if y > max_height - line_h:
            break
        # default attrs
        py5.no_fill()
        if fp in scroll['selection']:
            py5.fill(SELECTED_FILL)
        py5.stroke(0)
        py5.stroke_weight(4)            
        if fp.is_file():
            py5.no_stroke() # turn off border on files by default
        if i != 0 and thumb:
            py5.image(thumb, x + margin, y, rw, rh)
        # on mouse over, border on for everything 
        if mouse_over(x, y, rw, rh):
            # files are clickable only if a key is pressed
            py5.stroke(CLICKABLE)
            if fp.is_file() and not py5.is_key_pressed:
                py5.stroke(OVER)
            over = i
        # draws rect on folders and mouse-overed files
        py5.rect(x + margin, y, rw, rh)
        if i == 0:
            arrow(x + margin, y, rw, rh)
        py5.fill(0)
        if fp in scroll['selection']:
            py5.fill(255)
        py5.text_align(py5.CENTER)
        py5.text(name, x + rw / 2 + margin, y + rh + margin)
        # move on position
        x += rw + margin
        i += 1
    scroll['end'] = i

def arrow(x, y, rw, image_h):
    with py5.push():
        py5.translate(x, y)
        py5.line(rw / 2, margin,
                 rw / 2, image_h -margin)
        py5.line(margin, image_h / 2,
                 rw / 2, margin)
        py5.line(rw - margin, image_h / 2,
                 rw / 2, margin)

def update_files(folder, sort_key=None):
    global current_folder
    current_folder = folder
    py5.window_title(folder.name)
    files.clear()
    back_to_parent = [[folder.parent.name[:30], folder.parent, False]]
    files[:] = back_to_parent + list_files(folder, sort_key=None)

def list_files(folder, sort_key=None):
    try:
        items = [
            [fp.name[:30], fp, valid_image(fp)]
            for fp in sorted(Path(folder).iterdir(), key=sort_key)
            if fp.name[0] != '.' or hidden_files
            ]
        return items
    except IOError as e:
        print(e)
        return []

@lru_cache(maxsize=64)
def get_picture(path):
    if path.is_dir():
        return dir_image(path)
    try:
        if path.suffix.lower() == '.svg':
            return py5.convert_image(path)
    except RuntimeError as e:
        if DEBUG:
            print(f'{e}\nCould not load SVG from {path}')
    if valid_image(path):
        try:
            img = PIL.Image.open(path)
            ratio = img.width / img.height
            w = image_h * ratio
            img.thumbnail((w, image_h))
            return py5.convert_image(img)
        except Exception as e:
            if DEBUG:
                print(f'{e}\nCould not open {path}')
    suf = path.suffix.lower()[1:]
    if img := icon_imgs.get(suf):
        return img
    if DEBUG:
        print(f'Could not load icon for {path.name}.')
    return icon_imgs['zero']

def load_icon_imgs():
    global icon_imgs
    icon_imgs = {}
    try:
        with ZipFile(ICONS_ZIP) as icons:
            for f in sorted(icons.namelist()[1:]):
                img = PIL.Image.open(icons.open(f))
                py5image = py5.convert_image(img)
                suf = f.split('/')[1].split('.')[0]
                # print(suf) # for debug
                icon_imgs[suf] = py5image
    except FileNotFoundError:
        print('icons.zip missing!')
        py5.exit_sketch()

def dir_image(path):
    files = list_files(path)
    for name, fp, is_valid_img in files:
        if is_valid_img and fp.stem == path.stem:
            return get_picture(fp)
    for name, fp, is_valid_img in files:
        if is_valid_img:
            return get_picture(fp)
    icon = py5.create_graphics(128, 128)
    icon.begin_draw()
    icon.image(icon_imgs['folder'], 0, 0, 128, 128)
    x = 24
    for name, fp, _ in files[:5]:
        img = None
        if fp.is_file():
            img = get_picture(fp)
        elif fp.is_dir():
            img = icon_imgs['folder']
        if not img:
            continue
        icon.image(img, x, x, 48, 48)
        x += 10
    icon.end_draw()
    return icon 

def valid_image(path):
    # crude
    if path.suffix.lower() in (
        '.png', '.gif', '.jpg', '.jpeg'
        '.tga', '.webp', '.tif', '.tiff'
        ):
        return True
    return False

def open_path(path):
    if sys.platform == 'darwin':
        subprocess.Popen(['open', path])
    elif sys.platform == 'linux':
        subprocess.Popen(['xdg-open', path])
    else:
        subprocess.Popen(['explorer', path])

def save_selection():
    py5.save_strings(scroll['selection'], SELECTION)

def key_pressed():
    if py5.key == 'o':
        py5.select_folder('Select a folder', update_files)
    elif py5.key == 'h':
        global hidden_files
        hidden_files = not hidden_files
        update_files(current_folder)
    elif py5.key == 'u':
        if  current_folder == Path.home():
            update_files(Path.cwd())
        else:
            update_files(Path.home())
    elif py5.key == 'm':
        change_mode()
    elif py5.key == 's':
        change_sort()

def change_mode():
    if mode['mode'] == 'browse':
        mode['mode'] = 'browse_preview'
        py5.window_resize(py5.width + py5.height, py5.height)
    elif mode['mode'] == 'browse_preview':
        mode['mode'] = 'browse'
        py5.window_resize(py5.width - py5.height, py5.height)

def change_sort():
    if mode['sort_by'] == 'name':
        mode['sort_by'] = 'type'
        files.sort(key=by_type)
    elif mode['sort_by'] == 'type':
        mode['sort_by'] = 'name'
        files.sort(key=by_name)

    
def by_name(item):
    name, fp, _ = item
    if fp == current_folder.parent:
        return ''
    return name

def by_type(item):
    name, fp, _ = item
    if fp == current_folder.parent:
        return '', ''
    return fp.suffix, name

def mouse_over(x, y, rw, image_h):
    return x < py5.mouse_x < x + rw and y < py5.mouse_y < y + image_h

def mouse_clicked():
    if over is not None:
        name, fp, _ = files[over]
        if py5.mouse_button == py5.RIGHT:
            open_path(fp)
        elif (py5.is_key_pressed and
              py5.key_code == py5.CONTROL):
            if fp in scroll['selection']:
                scroll['selection'].remove(fp)
            else:
                scroll['selection'].append(fp)
                save_selection()
        elif (py5.is_key_pressed and
              py5.key_code == py5.SHIFT):
            scroll['selection'].clear()
            scroll['selection'].append(fp)
            save_selection()
        elif fp.is_dir():
            spf = scroll['last_scroll']
            if over == 0 and spf:
                scroll.update(spf.pop())
            else:
                spf.append(scroll.copy())
                scroll['start'] = 0
            files.clear()
            update_files(fp)
    else:
        if py5.mouse_button == py5.RIGHT:
            open_path(current_folder)

def mouse_wheel(e):
    delta = e.get_count()
    # print(scroll)
    if mode['mode'] != 'diff':
        if py5.mouse_x < max_width:
            if delta > 0 and scroll['end'] < len(files):
                scroll['start'] += scroll['first_row']
                scroll['previous_row'].append(scroll['first_row'])
            if delta < 0 and scroll['start'] > 0:
                scroll['start'] -= scroll['previous_row'].pop()

if __name__ == '__main__':
    py5.run_sketch(block=False)