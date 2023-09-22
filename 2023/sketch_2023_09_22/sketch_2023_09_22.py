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
    #py5.no_loop()

def draw():
    global over
    over = None
    py5.background(BACKGROUND)
    i = start
    x = y = 0
    while i < len(files) and y < py5.height:
        name, _, _, thumb = files[i]
        w = coll_w
        if mouse_over(x, y):
            py5.fill(SELECTED)
            files[i][2] = True
        else:
            py5.fill(255)
            files[i][2] = False
        if isinstance(thumb, py5.Py5Image):
            py5.image(thumb, x + 12, y, coll_w - 24, line_h - 24)
            w, h = thumb.width, thumb.height
        elif isinstance(thumb, py5.Py5Shape):
            py5.shape(thumb, x + 12, y, coll_w - 24, line_h - 24)
            w, h = thumb.get_width(), thumb.get_height()
        elif thumb == '<parent>':
            with py5.push_style():
                py5.stroke_weight(5)
                py5.line(x + coll_w / 2, y + 24, x + coll_w / 2, y + line_h * 0.8)
                py5.line(x + 24, line_h / 2, x + coll_w / 2, y + 24)
                py5.line(x + coll_w - 24, line_h / 2, x + coll_w / 2, y + 24)
        else:
            py5.rect(x + 12, y, coll_w - 24, line_h - 24)
        py5.fill(0)
        py5.text_align(py5.CENTER)
        py5.text(name, x + coll_w / 2, y + line_h - 12)
        x += coll_w
        if x > py5.height - 10:
            x = 0
            y += 200
        i += 1
        # print(i, '', end='')

def mouse_over(x, y):
    return x < py5.mouse_x < x + coll_w and y < py5.mouse_y < y + line_h

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
            #print(str(e))
            return None



def key_pressed():
    if py5.key == 'o':
        files.clear()
        py5.select_folder('Select a folder', list_files)

def get_icon(filename, size):
    # https://stackoverflow.com/a/40831294/19771
    import os , gi
    gi.require_version('Gtk', '3.0')
    from gi.repository import Gio , Gtk
    
    final_filename = ""
    if os.path.exists(filename):
        file = Gio.File.new_for_path(str(filename))
        info = file.query_info('standard::icon' , 0 , Gio.Cancellable())
        icon = info.get_icon().get_names()[0]

        icon_theme = Gtk.IconTheme.get_default()
        icon_file = icon_theme.lookup_icon(icon , size , 0)
        if icon_file != None:
            final_filename = icon_file.get_filename()
        return final_filename


py5.run_sketch(block=False)


