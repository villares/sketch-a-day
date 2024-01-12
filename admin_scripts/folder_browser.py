#! /home/villares/apps/thonny/bin/python3

"""
A naive folder/image browser experiment with py5 and Pillow
('diff' mode depends on folder_diff.py).

(c) Alexandre B A Villares - License: GPLv3

Images with thick borders are clickable folders.
(it displays images from inside the subfolders)
Left-click to navigate folders.
Right-click to open files/folders with OS.

SHIFT/CONTROL + click to select/desselect items.

's' to toggle sorting by name or by file extension
'r' to toggle reversed sorting 
'm' (WIP) to toggle modes 'browse only' 'preview' 'diff'

TODO:
   -[/] Implement image/tex/code preview in preview mode
       -[X] First attempt at image preview
       -[ ] Add folder image preview? refactor thumbnail's code?
       -[ ] Add text/code preview
       -[ ] Decide about mouse_over/selection behavior
   -[/] Implement diff mode using code from folder_diff.py
       -[ ] Debug! 
       -[ ] Improve folder_diff.py sketch selection/aquisition feature
       - Currently saves selection in folder_browser_selection.txt
         which can be used by standalone folder_diff.py too.
"""
import sys
import subprocess
from pathlib import Path
from zipfile import ZipFile
from functools import lru_cache
from itertools import cycle

import py5
import PIL.Image

import folder_diff

ICONS_ZIP = Path(__file__).parent / 'folder_browser_icons.zip'
SAVED_SELECTION = Path(__file__).parent / 'folder_browser_selection.txt'
BACKGROUND = py5.color(128, 128, 150)
CLICKABLE = py5.color(0, 0, 255)
OVER = py5.color(255)
SELECTED_FILL = py5.color(255, 64)
DEBUG = False

if DEBUG:
    print(f'Running on: {sys.executable}')

margin = 16
line_height = 160
col_width = 160

state = {
    #    'sort_by': by_name,  # function by_name has to be defined yet
    'sort_reversed': False,
    'mode': 'browse',
    'selection': [],
}

scroll = {
    'scroll_start': 0,
    'scroll_end': 0,
    'first_row': 0,
    'previous_row': [0],
    'last_scroll': [],
}

window_size = {
    'browse': (840, 840),
    'browse_preview': (1680, 840),
    'diff': (1680, 840),
}

hidden_files = False
folder_items = []


def setup():
    py5.size(840, 840)
    py5.window_resizable(True)
    load_icon_images()
    # set up global mode_options and sorting_options
    global sorting_options, mode_options
    mode_options = cycle(['browse_preview', 'diff', 'browse'])
    # sorting functions must have been defined previously
    sorting_options = cycle([by_name, by_type])
    state['sort_by'] = by_name
    update_items(Path.cwd())
    try:
        selection_strings = py5.load_strings(SAVED_SELECTION)
        state['selection'] = [Path(p) for p in selection_strings]
    except RuntimeError as e:
        print(e)
    folder_diff.setup_folder_diff()
    

def draw():
    py5.background(BACKGROUND)
    if state['mode'] == 'diff':
        folder_diff.draw()
    elif state['mode'] == 'browse':
        draw_browser()
    else:
        draw_browser(preview=True)
        
def draw_browser(preview=False):
    global over, max_width
    max_width = py5.width - py5.height if preview else py5.width
    max_height = py5.height
    selection = state['selection'] 
    # draw preview
    if  preview and selection:
        preview_size = py5.height - margin * 2
        if img := image_preview(selection[-1], preview_size):
            py5.image(img, max_width, margin)
    
    over = None
    i = scroll['scroll_start']
    x = 0
    y = margin
    first_row = True
    while i < len(folder_items):
        image_width = image_height = col_width - margin * 2
        name, fp, is_valid_img = folder_items[i]
        if len(name) > 25:
            name = f'{name[:15]}…{name[-8:]}'
        thumb = None
        # skipping first element, get thumb dims, if possible
        if i != 0 and (thumb := get_image(fp)):
            w, h = thumb.width, thumb.height
            ratio = w / h
            image_width = image_height * ratio
            if image_width > max_width - margin * 2:
                image_width = max_width - margin * 2
                image_height = image_width / ratio
        # move to next row and record first row length
        if x > max_width - image_width - margin:
            x = 0
            y += line_height
            if first_row:
                scroll['first_row'] = i - scroll['scroll_start']
                first_row = False
        # stop if position outside screen
        if y > max_height - line_height:
            break
        # default attrs
        py5.no_fill()
        if fp in selection:
            py5.fill(SELECTED_FILL)
        py5.stroke(0)
        py5.stroke_weight(4)
        if fp.is_file():
            py5.no_stroke()   # turn off border on files by default
        if i != 0 and thumb:
            py5.image(thumb, x + margin, y, image_width, image_height)
        # on mouse over, border on for everything
        if mouse_over(x, y, image_width, image_height):
            # files are clickable only if a key is pressed
            py5.stroke(CLICKABLE)
            if fp.is_file() and not py5.is_key_pressed:
                py5.stroke(OVER)
            over = i
        # draws rect on folders and mouse-overed files
        py5.rect(x + margin, y, image_width, image_height)
        if i == 0:
            arrow(x + margin, y, image_width, image_height)
        py5.fill(0)
        if fp in selection:
            py5.fill(255)
        py5.text_align(py5.CENTER)
        py5.text(name, x + image_width / 2 + margin, y + image_height + margin)
        # move on position
        x += image_width + margin
        i += 1
    scroll['scroll_end'] = i


def arrow(x, y, image_w, image_h):
    with py5.push():
        py5.translate(x, y)
        py5.line(image_w / 2, margin, image_w / 2, image_h - margin)
        py5.line(margin, image_h / 2, image_w / 2, margin)
        py5.line(image_w - margin, image_h / 2, image_w / 2, margin)


def update_items(folder=None):
    global current_folder
    current_folder = folder or current_folder
    py5.window_title(current_folder.name)
    folder_items.clear()
    back_to_parent = [[current_folder.parent.name, current_folder.parent, False]]
    folder_items[:] = back_to_parent + list_items(current_folder)

def list_items(folder):
    try:
        items = [
            [fp.name, fp, valid_image(fp)]
            for fp in sorted(
                Path(folder).iterdir(),
                key=state['sort_by'],
                reverse=state['sort_reversed']
                )
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
    image_height = line_height - 2 * margin
    try:
        img = PIL.Image.open(path)
        ratio = img.width / img.height
        image_width = image_height * ratio
        img.thumbnail((image_width, image_height))
        return py5.convert_image(img)
    except Exception as e:
        if DEBUG:
            print(f'{e}\nCould not open {path}')

@lru_cache(maxsize=64)
def image_preview(path, preview_size):
    if path.suffix.lower() == '.svg':
        if svg_img := image_from_svg(path):
            return svg_img
    try:
        img = PIL.Image.open(path)
        img.thumbnail((preview_size, preview_size))
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
    py5.save_strings(state['selection'], SAVED_SELECTION)


def key_pressed():
    if py5.key == 'm':
        toggle_modes()
    elif state['mode'] == 'diff':
        folder_diff.key_pressed()
    else:
        if py5.key == 'o':
            py5.select_folder('Select a folder', update_items)
        elif py5.key == 'h':
            global hidden_files
            hidden_files = not hidden_files
            update_items(current_folder)
        elif py5.key == 'u':
            if (current_folder == Path.home() and
                current_folder != Path.cwd()):
                update_items(Path.cwd())
            elif current_folder == Path.cwd():
                update_items(Path(__file__).parent.absolute().parent)
            else:
                update_items(Path.home())
        elif py5.key == 's':
            state['sort_by'] = next(sorting_options)
            update_items()
        elif py5.key == 'r':
            state['sort_reversed'] = not state['sort_reversed']
            update_items()
            
def toggle_modes():
    window_size[state['mode']] = (py5.width, py5.height)
    state['mode'] = next(mode_options)
    py5.window_resize(*window_size[state['mode']])
    if state['mode'] == 'diff':
        folder_diff.image_paths[:] = state['selection'] 
        folder_diff.walk_images(0)

def by_name(item):
    if item == current_folder.parent:
        return ''
    return item.name


def by_type(item):
    if item == current_folder.parent:
        return '', ''
    return item.suffix, item.name


def mouse_over(x, y, image_w, image_h):
    return x < py5.mouse_x < x + image_w and y < py5.mouse_y < y + image_h


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
            spf = scroll['last_scroll']
            if over == 0 and spf:
                scroll.update(spf.pop())
            else:
                spf.append(scroll.copy())
                scroll['scroll_start'] = 0
            folder_items.clear()
            update_items(fp)
    elif state['mode'] != 'diff':
        if py5.mouse_button == py5.RIGHT:
            open_path(current_folder)


def mouse_wheel(e):
    delta = e.get_count()
    if state['mode'] == 'diff':
        folder_diff.scroll_offset += delta
    else:
        if py5.mouse_x < max_width:
            if delta > 0 and scroll['scroll_end'] < len(folder_items):
                scroll['scroll_start'] += scroll['first_row']
                scroll['previous_row'].append(scroll['first_row'])
            if delta < 0 and scroll['scroll_start'] > 0:
                scroll['scroll_start'] -= scroll['previous_row'].pop()
        

if __name__ == '__main__':
    py5.run_sketch(block=False)
