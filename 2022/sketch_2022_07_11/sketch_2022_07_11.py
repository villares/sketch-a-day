import os
import io
import PIL.Image
import py5

current = 0
previous = None


def setup():
    global image_paths
    #py5.full_screen()
    py5.size(1600, 1000)
    folder = '/home/villares/GitHub/sketch-a-day/2022/sketch_2022_07_10/'
    try:
        file_list = sorted(os.listdir(folder))  # get list of files in folder
    except:
        file_list = []
    image_paths = [os.path.join(folder, f) for f in file_list
                   if os.path.isfile(os.path.join(folder, f))
                   and f.lower().endswith(('.png', '.jpg', 'jpeg',
                                      '.tiff', '.bmp', '.gif'))]
    walk_images(0)
    #py5.text_font(py5.create_font('Inconsolata Bold', 14))
    py5.text_font(py5.create_font('Source Code Pro', 12))

def draw():
    py5.background(240)
    py5.image(img, 50, 50)
    code = info['code']
    py5.fill(0)
    py5.text(code.replace('    \n', '\n').replace('\n\n\n', ''), 1000, 100)
    py5.text(image_paths[current], 50, 30)
    py5.save(f'{current}.png')
    walk_images(1)
    if current == 0:
        py5.exit_sketch()

def key_pressed():
    if py5.key == py5.ESC:
        py5.exit_sketch()
    elif py5.key_code == py5.DOWN:
        walk_images(1)
    elif py5.key_code == py5.UP:
        walk_images(-1)


def walk_images(i):
    global img, info, current
    current = (current + i) % len(image_paths)
    img, info = load_image_and_data(current)
    #print(current)

def load_image_and_data(i, resize=None):
    img = PIL.Image.open(image_paths[i])
    cur_width, cur_height = img.size
    if resize:
        new_width, new_height = resize
        scale = min(new_height / cur_height, new_width / cur_width)
        img = img.resize(
            (int(cur_width * scale), int(cur_height * scale)),
            PIL.Image.Resampling.LANCZOS,
        )
    return py5.convert_image(img), img.info

py5.run_sketch()
