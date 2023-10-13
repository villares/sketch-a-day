#!/home/villares/thonny-python-env/bin/python3

"""
A naive folder/image browser experiment that depends
on py5 and Pillow.

(c) Alexandre B A Villares - License: GPLv3

Images with thick borders are clickable folders.
(it displays images from inside the subfolders)
Left-click to navigate folders.
Right-click to open files/folders with OS.

SHIFT/CONTROL + click to select/desselect items.

's' to toggle sorting by name or by file extension
'm' (WIP) to toggle modes 'browse only' 'preview' 'diff'

TODO:
   -[ ] Implement image/tex/code preview in preview mode
   -[ ] Implement diff mode using code from folder_diff.py
   -[X] Create a "selected items list" feature
       - Currently saves selection in
         folder_browser_selection.txt
         which can be used by folder_diff.py
       - Adapt for internal 'diff mode'
"""
import sys
import subprocess
from pathlib import Path
from zipfile import ZipFile
from functools import lru_cache
from itertools import cycle

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

margin = 16
line_h = 160
image_h = line_h - margin * 2
coll_w = 160

state = {
#    'sort_by': by_name,  # function by_name has to be defined yet
    'mode': 'browse',
    'size': {
        'browse': (840, 840),
        'browse_preview': (1680, 840),
        'diff': (1680, 840),
        },
    'scroll_start': 0,
    'scroll_end': 0,
    'first_row': 0,
    'previous_row': [0],
    'last_state': [],
    'selection': [],
}

hidden_files = False
folder_items = []


def setup():
    py5.size(840, 840)
    py5.text_align(py5.LEFT, py5.TOP)
    py5.window_resizable(True)
    load_icon_images()
    # set up global sorting_options and mode_options
    global sorting_options, mode_options
    mode_options = cycle(['browse_preview', 'diff', 'browse'])
    # sorting functions must have been defined previously
    sorting_options = cycle([by_name, by_type])
    toggle_sorting() # needs to be called once on setup
    # toggle_modes should not be called because it resizes window
    update_items(Path.cwd())


def draw():
    py5.background(BACKGROUND)
    if state['mode'] != 'diff':
        draw_browser()
    else:  # not implemented
        draw_diff()


def draw_browser():
    global over, max_width
    over = None
    if state['mode'] == 'browse':
        max_width = py5.width
        max_height = py5.height
    if state['mode'] == 'browse_preview':
        max_width = py5.width - py5.height
        max_height = py5.height
    i = state['scroll_start']
    x = 0
    y = margin
    first_row = True
    while i < len(folder_items):
        rw = rh = coll_w - margin * 2
        name, fp, is_valid_img = folder_items[i]
        if len(name) > 25:
            name = f'{name[:15]}…{name[-8:]}'
        thumb = None
        # skipping first element, get thumb dims, if possible
        if i != 0 and (thumb := get_image(fp)):
            w, h = thumb.width, thumb.height
            ratio = w / h
            rw, rh = image_h * ratio, image_h
            if rw > max_width - margin * 2:
                rw = max_width - margin * 2
                rh = rw / ratio
        # move to next row and record first row length
        if x > max_width - rw - margin:
            x = 0
            y += line_h
            if first_row:
                state['first_row'] = i - state['scroll_start']
                first_row = False
        # stop if position outside screen
        if y > max_height - line_h:
            break
        # default attrs
        py5.no_fill()
        if fp in state['selection']:
            py5.fill(SELECTED_FILL)
        py5.stroke(0)
        py5.stroke_weight(4)
        if fp.is_file():
            py5.no_stroke()   # turn off border on files by default
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
        if fp in state['selection']:
            py5.fill(255)
        py5.text_align(py5.CENTER)
        py5.text(name, x + rw / 2 + margin, y + rh + margin)
        # move on position
        x += rw + margin
        i += 1
    state['scroll_end'] = i


def draw_diff():
    pass


def arrow(x, y, rw, image_h):
    with py5.push():
        py5.translate(x, y)
        py5.line(rw / 2, margin, rw / 2, image_h - margin)
        py5.line(margin, image_h / 2, rw / 2, margin)
        py5.line(rw - margin, image_h / 2, rw / 2, margin)


def update_items(folder):
    global current_folder
    current_folder = folder
    py5.window_title(folder.name)
    folder_items.clear()
    back_to_parent = [[folder.parent.name, folder.parent, False]]
    folder_items[:] = back_to_parent + list_items(folder)
    folder_items.sort(key=state['sort_by'])

def list_items(folder, sort_key=None):
    try:
        items = [
            [fp.name, fp, valid_image(fp)]
            for fp in sorted(Path(folder).iterdir())
            if fp.name[0] != '.' or hidden_files
        ]
        return items
    except IOError as e:
        print(e)
        return []


def get_image(path):
    if path.is_dir():
        return folder_image(path)
    if path.suffix.lower() == '.svg':
        if svg_img := image_from_svg(path):
            return svg_img
    if valid_image(path):
        if thumb_img := image_thumbnail(path):
            return thumb_img
    if icon_image := icon_images.get(path.suffix.lower()[1:]):
        return icon_image
    if DEBUG:
        print(f'Could not load specific icon for {path.name}.')
    return icon_images['zero']  # generic empty icon


@lru_cache(maxsize=64)
def image_from_svg(path):
    try:
        return py5.convert_image(path)
    except RuntimeError as e:
        if DEBUG:
            print(f'{e}\nCould not load SVG from {path}')    
    return None 


@lru_cache(maxsize=64)
def image_thumbnail(path):
    try:
        img = PIL.Image.open(path)
        ratio = img.width / img.height
        w = image_h * ratio
        img.thumbnail((w, image_h))
        return py5.convert_image(img)
    except Exception as e:
        if DEBUG:
            print(f'{e}\nCould not open {path}')

def load_icon_images():
    global icon_images
    icon_images = {}
    try:
        with ZipFile(ICONS_ZIP) as icons:
            for f in sorted(icons.namelist()[1:]):
                img = PIL.Image.open(icons.open(f))
                py5image = py5.convert_image(img)
                suf = f.split('/')[1].split('.')[0]
                # print(suf) # for debug
                icon_images[suf] = py5image
    except FileNotFoundError:
        print('icons.zip missing!')
        py5.exit_sketch()

@lru_cache(maxsize=64)
def folder_image(path):
    folder_items = list_items(path)
    for name, fp, is_valid_img in folder_items:
        if is_valid_img and fp.stem == path.stem:
            return get_image(fp)
    for name, fp, is_valid_img in folder_items:
        if is_valid_img:
            return get_image(fp)
    return compose_folder_icon(folder_items)    
        
def compose_folder_icon(files):        
    icon = py5.create_graphics(128, 128)
    icon.begin_draw()
    icon.image(icon_images['folder'], 0, 0, 128, 128)
    x = 24
    for name, fp, _ in files[:5]:
        img = None
        if fp.is_file():
            img = get_image(fp)
        elif fp.is_dir():
            img = icon_images['folder']
        if not img:
            continue
        icon.image(img, x, x, 48, 48)
        x += 10
    icon.end_draw()
    return icon


def valid_image(path):
    # crude
    if path.suffix.lower() in (
        '.png',
        '.gif',
        '.jpg',
        '.jpeg',
        '.tga',
        '.webp',
        '.tif',
        '.tiff',
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
    py5.save_strings(state['selection'], SELECTION)


def key_pressed():
    if py5.key == 'o':
        py5.select_folder('Select a folder', update_items)
    elif py5.key == 'h':
        global hidden_files
        hidden_files = not hidden_files
        update_items(current_folder)
    elif py5.key == 'u':
        if current_folder == Path.home():
            update_items(Path.cwd())
        else:
            update_items(Path.home())
    elif py5.key == 'm':
        toggle_modes()
    elif py5.key == 's':
        toggle_sorting()


def toggle_modes():
    state['size'][state['mode']] = (py5.width, py5.height)
    state['mode'] = next(mode_options)
    py5.window_resize(*state['size'][state['mode']])


def toggle_sorting():
    state['sort_by'] = next(sorting_options)
    folder_items.sort(key=state['sort_by'])


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
        name, fp, _ = folder_items[over]
        if py5.mouse_button == py5.RIGHT:
            open_path(fp)
        elif py5.is_key_pressed and py5.key_code == py5.CONTROL:
            if fp in state['selection']:
                state['selection'].remove(fp)
            else:
                state['selection'].append(fp)
                save_selection()
        elif py5.is_key_pressed and py5.key_code == py5.SHIFT:
            state['selection'].clear()
            state['selection'].append(fp)
            save_selection()
        elif fp.is_dir():
            spf = state['last_state']
            if over == 0 and spf:
                state.update(spf.pop())
            else:
                spf.append(state.copy())
                state['scroll_start'] = 0
            folder_items.clear()
            update_items(fp)
    else:
        if py5.mouse_button == py5.RIGHT:
            open_path(current_folder)


def mouse_wheel(e):
    delta = e.get_count()
    # print(state)
    if state['mode'] != 'diff':
        if py5.mouse_x < max_width:
            if delta > 0 and state['scroll_end'] < len(folder_items):
                state['scroll_start'] += state['first_row']
                state['previous_row'].append(state['first_row'])
            if delta < 0 and state['scroll_start'] > 0:
                state['scroll_start'] -= state['previous_row'].pop()


if __name__ == '__main__':
    py5.run_sketch(block=False)
