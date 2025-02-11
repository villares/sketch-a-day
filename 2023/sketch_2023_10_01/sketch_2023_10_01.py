import PIL.Image
import py5
import difflib
from pathlib import Path

SELECTION = Path('/home/villares/GitHub'
                      '/sketch-a-day/admin_scripts'
                      '/folder_browser_selection.txt')

image_paths = []
img = None
current = 0
code = previous_code = ''
font_size, line_step = 12, 12
run = False
diff = True
scroll_offset = 0

def setup():
    global fr, fb
    py5.size(1800, 1000)
    image_paths[:] = py5.load_strings(SELECTION)
    walk_images(0)
    fr = py5.create_font("Source Code Pro", font_size)
    fb = py5.create_font("Source Code Pro Bold", font_size)

def draw():
    py5.background(240)
    if image_paths and img:
        py5.image(img, 50, 50)
        draw_code(img.width + 100, 80)
        py5.no_stroke()
        py5.fill(240)
        py5.rect(0, 0, py5.width, 50)
        py5.fill(0)
        py5.text(image_paths[current], 50, 30)
        if diff:
            py5.fill(0, 100, 0)
            py5.text('previous:' + image_paths[previous], 600, 30)

    if run:
        py5.save(f'a-{current}-{current_path.stem}.png')
        walk_images(1)
        if current == 0:
            py5.exit_sketch()

def walk_images(i):
    global current, previous, img, code, previous_code
    if len(image_paths) == 0:
        return
    previous, current = current, (current + i) % len(image_paths)
    current_path = Path(image_paths[current])
    img, new_code = get_img_and_code(current_path)
    previous_code, code = code, new_code

def get_img_and_code(path, resize=(900, 900)):
    img, code = None, ''
    if path.is_file():
        img, code = load_image_and_data(path, resize)
    elif path.is_dir():
        image_path = path / (path.name + '.png')
        img, code = load_image_and_data(image_path, resize)
        if len(code) == 0:
            code_path = path / (path.name + '.py')
            code = code_path.read_text()
    return img, code
    
def load_image_and_data(image_file, resize=None):
    img = PIL.Image.open(image_file)
    cur_width, cur_height = img.size
    if resize:
        new_width, new_height = resize
        sf = min(new_height / cur_height, new_width / cur_width)
        img = img.resize((int(cur_width * sf), int(cur_height * sf)),
                              PIL.Image.Resampling.LANCZOS)
    code = img.info.get('code', '').replace('    \n', '\n').replace('\n\n\n', '')
    return py5.convert_image(img), code

def list_files(folder):
    global image_paths
    try:
        file_list = sorted(Path(folder).iter_dir())  # get list of files in folder
    except:
        file_list = []
    image_paths = [
            f for f in file_list
            if f.isfile() and f.suffix.lower()
            in ('.png', '.jpg', 'jpeg', '.tga', '.webp',
               '.tiff', '.tif', '.bmp', '.gif')]

def draw_code(x, y):
    with py5.push():
        py5.translate(0, line_step * scroll_offset)
        py5.text_font(fb)
        differ = difflib.Differ()
        colors = {' ': 0, '-': 0xFFFF0000, '+': 0xFF0000FF, '?': 0xFF00CC00}
        if previous_code and diff:
            code_lines = differ.compare(previous_code.splitlines(), code.splitlines())
        else:
            code_lines = code.splitlines()
        for li in code_lines:
            py5.fill(colors.get(li[:1], 0))
            py5.text(li, x, y)
            py5.translate(0, line_step )
    

def key_pressed():
    global run, current, previous, previous_code, diff
    global scroll_offset
    if py5.key == 'o':
        py5.select_folder('Select a folder', list_files)
    elif py5.key == 'u':
        image_paths[:] = py5.load_strings(SELECTION_PATH)
        previous_code = ''
        current = 0
        walk_images(0)
    elif py5.key == 'd':
        diff = not diff
    elif py5.key == 'p':
        current_path = Path(image_paths[current])
        py5.save(f'{current}-{current_path.stem}.png')
    elif py5.key == 'r':
        previous_code = ''
        current = 0
        run = True
    elif py5.key == py5.ESC:
        py5.exit_sketch()
    elif py5.key_code == py5.DOWN:
        walk_images(1)
    elif py5.key_code == py5.UP:
        walk_images(-1)
    elif py5.key_code == py5.LEFT:
        scroll_offset = 0


def mouse_wheel(e):
    global scroll_offset
    d = e.get_count()
    scroll_offset += d
 
if __name__ == '__main__':
    py5.run_sketch()

