from pathlib import Path

import py5
import imageio

BACKGROUND = py5.color(200, 200, 240)
SELECTED = py5.color(100, 100, 200)

files = []
line_h = 150
margin = 12
image_h = line_h - margin * 2
coll_w = 150
start = 0
over = None

def setup():
    py5.size(800, 800)
    py5.text_align(py5.LEFT, py5.TOP)
    list_files(Path.cwd().parent.parent)
    #py5.no_loop()

def draw():
    py5.background(BACKGROUND)
    i = start
    x = 0
    y = margin
    while i < len(files):
        name, _, _, thumb = files[i]
        rw = coll_w - margin * 2
        if isinstance(thumb, py5.Py5Image):
            w, h = thumb.width, thumb.height
            ratio = w / h
            rw = image_h * ratio
            func = py5.image
        elif isinstance(thumb, py5.Py5Shape):
            w, h = thumb.get_width(), thumb.get_height()
            func = py5.shape
        elif thumb == '<parent>':
            func = arrow
        else:
            func = lambda *args: None
            
        if x > py5.width - rw - margin :
            x = 0
            y += line_h
        if y > py5.height - line_h:
            break

        func(thumb, x + margin, y, rw, image_h)

        if mouse_over(x, y, rw, image_h):
            py5.fill(SELECTED, 100)
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
        # print(i, '', end='')

def mouse_over(x, y, rw, image_h):
    return x < py5.mouse_x < x + rw and y < py5.mouse_y < y + image_h

def list_files(folder):
    parent = folder.parent
    files[:] = [[parent.name[:30], parent, None, '<parent>']] + sorted(
        [f.name[:30], f, None, None]
        for f in Path(folder).iterdir()
        if f.name[0] != '.'
        )
    for i, (_, f, _, _) in enumerate(files[1:], 1):
        files[i][3] = get_thumbnail(f)

def mouse_pressed():
    for f in files:
        if f[2] and f[1].is_dir():
            print(f)
            files.clear()
            list_files(f[1])        

def get_thumbnail(path):
    if path.suffix.lower() in ('.png', '.jpg', '.jpeg', '.gif', '.tif'):
        return py5.load_image(path)
    elif path.suffix.lower() == '.svg':
        try:
            return py5.load_shape(path)
        except RuntimeError as e:
            return Nonw
    else:
        try:
            t = get_icon(path, 128)
            return py5.load_shape(t)
        except Exception as e:
            print(str(e))
            return None

def arrow(_, x, y, rw, image_h):
    with py5.push_style():
        py5.stroke_weight(5)
        py5.line(x + rw / 2, y + margin,
                 x + rw / 2, y + image_h - margin)
        py5.line(x + margin, image_h / 2 + margin,
                 x + rw / 2, y + margin)
        py5.line(x + rw - margin, image_h / 2 + margin,
                 x + rw / 2, y + margin)

def key_pressed():
    if py5.key == 'o':
        files.clear()
        py5.select_folder('Select a folder', list_files)

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


py5.run_sketch(block=False)


