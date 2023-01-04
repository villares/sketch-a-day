# using py5 (py5coding.org) imported mode

from PIL import Image
import io

def setup():
    size(517, 707)
    no_loop()

def draw():
#     img = Image.open('data/a.png', mode='r')  # se a imagem estiver em outro formato
#     with io.BytesIO() as bytes_io:
#         img.save(bytes_io, format='jpeg')
#         list_jpg_bytes = list(bytes_io.getvalue())

    with open('data/a.jpg', 'rb') as f:
        list_jpg_bytes = list(f.read())

    for _ in range(10):
        loc = random_int(len(list_jpg_bytes) - 1)
        list_jpg_bytes[loc] = random_int(1, 255)

    stream = io.BytesIO(bytes(list_jpg_bytes))
    new_img = Image.open(stream)
    try:
        image(convert_image(new_img), 0, 0) # PIL.Image to py5Image
    except: # OSError / UnidentifiedImageError:
        pass
    
def key_pressed():
    save_frame('###.png')
    redraw()