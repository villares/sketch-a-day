from pathlib import Path
from functools import lru_cache

import py5
from PIL import Image

BACKGROUND = py5.color(128, 128, 150)
SELECTED = py5.color(100, 100, 200, 100)

files = []
line_h = 150
margin = 12
image_h = line_h - margin * 2
coll_w = 150
items_range = {'start': 0, 'end': 0}
over = None

def setup():
    py5.size(800, 800)
    py5.text_align(py5.LEFT, py5.TOP)
    list_files(Path.cwd().parent.parent)
    #py5.no_loop()

def draw():
    py5.background(BACKGROUND)
    i = items_range['start']
    x = 0
    y = margin
    while i < len(files):
        name, f, _ = files[i]        
        thumb = get_picture(f)
        rw = coll_w - margin * 2
        if i == 0:
            func = arrow
        elif isinstance(thumb, py5.Py5Image):
            rw = thumb.width
            func = py5.image
        elif isinstance(thumb, py5.Py5Shape):
            w, h = thumb.get_width(), thumb.get_height()
            ratio = w / h
            rw = image_h * ratio
            func = py5.shape
        else:
            func = lambda *args: None
            
        if x > py5.width - rw - margin :
            x = 0
            y += line_h
        if y > py5.height - line_h:
            break

        func(thumb, x + margin, y, rw, image_h)

        if mouse_over(x, y, rw, image_h):
            py5.fill(SELECTED)
            files[i][2] = True
        else:
            py5.no_fill()
            files[i][2] = False
        
        py5.rect(x + margin, y, rw, image_h)
        py5.fill(0)
        py5.text_align(py5.CENTER)
        py5.text(name, x + rw / 2 + margin, y + image_h + margin)
        x += rw + margin
        i += 1
    items_range['end'] = i

def arrow(_, x, y, rw, image_h):
    with py5.push():
        py5.translate(x, y)
        py5.stroke_weight(5)
        py5.line(rw / 2, margin,
                 rw / 2, image_h -margin)
        py5.line(margin, image_h / 2,
                 rw / 2, margin)
        py5.line(rw - margin, image_h / 2,
                 rw / 2, margin)

def list_files(folder):
    items_range['start'] = 0
    parent = folder.parent
    files[:] = [[parent.name[:30], parent, False]] + sorted(
        [f.name[:30], f, False]
        for f in Path(folder).iterdir()
        if f.name[0] != '.'
        )
    
@lru_cache(maxsize=64)
def get_picture(path):
    if path.is_dir():
        return None
    if path.suffix.lower() == '.svg':
        try:
            return py5.load_shape(path)
        except RuntimeError as e:
            print(f'Could not load SVG from {path}')
    try:
        img = Image.open(path)
        ratio = img.width / img.height
        w = image_h * ratio
        img.thumbnail((w, image_h))
        return py5.convert_image(img)
    except Image.UnidentifiedImageError as e:
        pass
    try:
        t = get_icon(path, 128)
        return py5.load_shape(t)
    except RuntimeError as e:
        print(f'Could not load icon SVG for {path.name}.')
        return None

def get_icon(path, size):
    # https://stackoverflow.com/a/40831294/19771
    # sudo pacman -S python-gobject gtk4
    # pip install PyGObject
    import gi
    gi.require_version('Gtk', '3.0')
    from gi.repository import Gio , Gtk
    final_filename = ""
    if path.exists():
        file = Gio.File.new_for_path(str(path))
        info = file.query_info('standard::icon', 0, Gio.Cancellable())
        icon = info.get_icon().get_names()[0]
        icon_theme = Gtk.IconTheme.get_default()
        icon_file = icon_theme.lookup_icon(icon, size, 0)
        if icon_file != None:
            final_filename = icon_file.get_filename()
        return final_filename
        
def key_pressed():
    if py5.key == 'o':
        files.clear()
        py5.select_folder('Select a folder', list_files)

def mouse_over(x, y, rw, image_h):
    return x < py5.mouse_x < x + rw and y < py5.mouse_y < y + image_h

def mouse_pressed():
    for f in files:
        if f[2] and f[1].is_dir():
            files.clear()
            list_files(f[1])        

def mouse_wheel(e):
    delta = e.get_count()
    if (delta > 0 and items_range['end'] < len(files) - 1
        or delta < 0 and items_range['start'] > 0):
        items_range['start'] += delta

py5.run_sketch(block=False)


