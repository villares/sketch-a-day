#!/home/villares/thonny-python-env/bin/python3

"""
A naive image browser experiment.

TODO:
   - Create "selected item"
   - Check scrolling issues
"""

import sys
import subprocess
from pathlib import Path
from functools import lru_cache

import py5
from PIL import Image

BACKGROUND = py5.color(128, 128, 150)
CLICKABLE = py5.color(0, 0, 255)
OVER = py5.color(255)

hidden_files = False
files = []
line_h = 150
margin = 12
image_h = line_h - margin * 2
coll_w = 150
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
    global folder_icon
    py5.size(800, 800)
    py5.text_align(py5.LEFT, py5.TOP)
    update_files(Path.cwd())
#    t = get_icon_filename(Path.home().parent)
#    folder_icon = py5.convert_image(t)
    folder_icon = py5.load_image('folder.png')

def draw():
    global over
    over = None
    py5.background(BACKGROUND)
    i = scroll['start']
    x = 0
    y = margin
    first_row = True
    while i < len(files):
        rw = rh = coll_w - margin * 2
        name, f, valid_img = files[i]        
        thumb = None
        
        if i != 0 and (thumb:= get_picture(f)):
            w, h = thumb.width, thumb.height
            ratio = w / h
            rw, rh = image_h * ratio, image_h
            if rw > max_width - margin * 2:
                rw = max_width - margin * 2
                rh = rw / ratio
            
        if x > max_width - rw - margin :
            x = 0
            y += line_h
            if first_row:
                scroll['first_row'] = i - scroll['start']
                first_row = False
                
        if y > max_height - line_h:
            break
        
        py5.no_fill()
        py5.stroke(0)
        py5.stroke_weight(4)            
        if f.is_file():
            py5.no_stroke()
        if i != 0 and thumb:
            py5.image(thumb, x + margin, y, rw, rh)
        if mouse_over(x, y, rw, rh):
            py5.stroke(CLICKABLE)
            if f.is_file() and not py5.is_key_pressed:
                py5.stroke(OVER)
            over = i
        py5.rect(x + margin, y, rw, rh)
        if i == 0:
            arrow(x + margin, y, rw, rh)
        py5.fill(0)
        py5.text_align(py5.CENTER)
        py5.text(name, x + rw / 2 + margin, y + rh + margin)

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
    global current_folder
    current_folder = folder
    py5.window_title(folder.name)
    files.clear()
    back_to_parent = [[folder.parent.name[:30], folder.parent, False]]
    files[:] = back_to_parent + list_files(folder)

def list_files(folder):
    try:
        items = [
            [f.name[:30], f, valid_image(f)]
            for f in sorted(Path(folder).iterdir())
            if f.name[0] != '.' or hidden_files
            ]
#         for item in items:
#             print(item)
        return items
    except IOError as e:
        print(e)
        return []
    
@lru_cache(maxsize=64)
def get_picture(path):
    try:
        if path.is_dir():
            return dir_image(path)
        if path.suffix.lower() == '.svg':
            # TODO check possible resize
                return py5.convert_image(path)
    except RuntimeError as e:
            print(f'{e}\nCould not load SVG from {path}')
    if valid_image(path):
        try:
            img = Image.open(path)
            ratio = img.width / img.height
            w = image_h * ratio
            img.thumbnail((w, image_h))
            return py5.convert_image(img)
        except Exception as e:
            print(f'{e}\nCould not open {path}')
    try:
        t = get_icon_filename(path)
        img = py5.convert_image(t)
        return img
    except RuntimeError as e:
        print(f'{e}\nCould not load icon for {path.name}.')
        return None

def get_icon_filename(path, size=128):
    final_filename = ""
    if sys.platform == 'linux':
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
    return final_filename

def dir_image(path):
    files = list_files(path)
    for name, fp, valid_img in files:
        if valid_img and fp.stem == path.stem:
            return get_picture(fp)
    for name, fp, valid_img in files:
        if valid_img:
            return get_picture(fp)
    icon = py5.create_graphics(128, 128)
    icon.begin_draw()
    icon.image(folder_icon, 0, 0, 128, 128)
    x = 24
    for name, fp, _ in files[:5]:
        img = None
        if fp.is_file():
            img = get_picture(fp)
        elif fp.is_dir():
            img = folder_icon
        if not img:
            continue
        icon.image(img, x, x, 48, 48)
        x += 10
    icon.end_draw()
    return icon #folder_icon if img is None else img

# @cache  # only needed if you use the costly try: Image.open check
def valid_image(path):
    # crude
    if path.suffix.lower() in (
        '.png', '.gif', '.jpg', '.jpeg'
        '.tga', '.webp', '.tif', '.tiff'
        ):
        return True
#     # the if bellow is to reduce/avoid the costly try: Image.open(path)
#     if path.suffix.lower() in (
#         '.py', '.pyde', '.svg', '.txt'
#         '.md', '.pyc'
#         ):
#         return False
#     # a costly check if the thing is an image
#     try:
#         Image.open(path)
#         return True
#     except Exception:
#         return False    
    return False

def open_path(path):
    if sys.platform == 'darwin':
        subprocess.Popen(['open', path])
    elif sys.platform == 'linux':
        subprocess.Popen(['xdg-open', path])
    else:
        subprocess.Popen(['explorer', path])

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

def mouse_over(x, y, rw, image_h):
    return x < py5.mouse_x < x + rw and y < py5.mouse_y < y + image_h

def mouse_clicked():
    if over is not None:
        name, fp, _ = files[over]
        if (py5.mouse_button == py5.RIGHT
            or py5.is_key_pressed
            ):
            open_path(fp)
        elif fp.is_dir():
            spf = scroll['last_scroll']
            if over == 0 and spf:
                scroll.update(spf.pop())
            else:
                spf.append(scroll.copy())
                scroll['start'] = 0
            files.clear()
            #print(fp)
            update_files(fp)
    else:
        if (py5.mouse_button == py5.RIGHT or
            py5.is_key_pressed):
            open_path(files[0][1].parent)

def mouse_wheel(e):
    # print(scroll)
    delta = e.get_count()
    if delta > 0 and scroll['end'] < len(files):
        scroll['start'] += scroll['first_row']
        scroll['previous_row'].append(scroll['first_row'])
    if delta < 0 and scroll['start'] > 0:
        scroll['start'] -= scroll['previous_row'].pop()

py5.run_sketch(block=False)