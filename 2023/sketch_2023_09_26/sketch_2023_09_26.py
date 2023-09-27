"""
Extracting some icons
"""

from pathlib import Path
from functools import lru_cache, cache
import pickle

import py5
from PIL import Image

BACKGROUND = py5.color(128, 128, 150)
CLICKABLE = py5.color(0, 0, 255)
OVER = py5.color(255)

files = []
icons = set()
suffixes = {}

line_h = 75
margin = 12
image_h = line_h - margin * 2
coll_w = 75
max_width = 800
max_height = 800
scroll = {
    'start': 0,
    'end': 0,
    'first_row': 0,
    'previous_row': [0],
    'last_scroll': []
    }

def setup():
    py5.size(800, 800)
    py5.text_align(py5.LEFT, py5.TOP)
    #update_files(Path.cwd().parent.parent)
    #py5.no_loop()

def draw():
    global over
    over = None
    py5.background(BACKGROUND)
    i = scroll['start']
    x = 0
    y = margin
    first_row = True
    files = list(suffixes.items())
    while i < len(files):
        rw = rh = coll_w - margin * 2
        suffix, icon = files[i]
        thumb = None
                    
        if x > max_width - rw - margin :
            x = 0
            y += line_h
            if first_row:
                scroll['first_row'] = i - scroll['start']
                first_row = False
                
        if y > max_height - line_h:
            break
        
        thumb = get_picture(icon)
        if thumb:
            py5.image(thumb, x + margin, y, rw, rh)

        py5.fill(0)
        py5.text_align(py5.CENTER)
        py5.text(suffix, x + rw / 2 + margin, y + rh + margin)

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

def update_files(folder):
    py5.window_title(folder.name)
    files.clear()
    suffixes.clear()
    icons.clear()
    list_files(folder)

def list_files(folder):
    for f in Path(folder).iterdir():
        if f.name[0] != '.':
            try:
                if f.is_file():
                    suf, ico = f.suffix, get_icon_filename(f, 128)
                    if ico not in icons:
                        icons.add(ico)
                        suffixes[suf] = ico
                elif f.is_dir:
                    list_files(f)
            except IOError as e:
                print(str(e))
        
@lru_cache(maxsize=64)
def get_picture(path):
    try:
        #t = get_icon_filename(path, 128)
        img = py5.convert_image(path)
        return img
    except RuntimeError as e:
        print(f'Could not load icon SVG for {path}.')
        return None

def get_icon_filename(path, size):
    final_filename = ""
    # https://stackoverflow.com/a/40831294/19771
    # sudo pacman -S python-gobject gtk4
    # pip install PyGObject
    import gi
    gi.require_version('Gtk', '3.0')
    from gi.repository import Gio , Gtk
    if path.exists():
        file = Gio.File.new_for_path(str(path))
        info = file.query_info('standard::icon', 0, Gio.Cancellable())
        icon = info.get_icon().get_names()[0]
        icon_theme = Gtk.IconTheme.get_default()
        icon_file = icon_theme.lookup_icon(icon, size, 0)
        if icon_file != None:
            final_filename = icon_file.get_filename()
            #print(final_filename)
    return final_filename

# @cache  # only needed if you use the costly try: Image.open check
def valid_image(path):
    # crude
    if path.suffix.lower() in (
        '.png', '.gif', '.jpg', '.jpeg'
        '.tga', '.webp', '.tif', '.tiff'
        ):
        return True


def key_pressed():
    if py5.key == 'o':
        py5.select_folder('Select a folder', update_files)

def mouse_wheel(e):
    # print(scroll)
    delta = e.get_count()
    if delta > 0 and scroll['end'] < len(files) - scroll['first_row']:
        scroll['start'] += scroll['first_row']
        scroll['previous_row'].append(scroll['first_row'])
    if delta < 0 and scroll['start'] > 0:
        scroll['start'] -= scroll['previous_row'].pop()

py5.run_sketch(block=False)





