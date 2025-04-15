from itertools import product
from random import shuffle
import py5

url = 'https://upload.wikimedia.org/wikipedia/commons/c/cb/Mapa_de_S%C3%A3o_Paulo_-_1924.jpg'
S = 24
tiles = []

def setup():
    global img, fonts
    py5.size(700, 700)
    py5.text_align(py5.CENTER, py5.CENTER)

    img = py5.load_image(url)
    # Get Tomorrow from 
    fonts = [py5.create_font(name, 12)
             for name in py5.Py5Font.list()
             if 'Tomorrow Bold' in name]
    py5.text_font(fonts[0])
    start()
    
def start():
    x = py5.random_int(img.width - py5.width)
    y = py5.random_int(img.height - py5.height)
    for n, (i, j) in enumerate(product(range(7), repeat=2), 1):
        result = img.get_pixels(x + i * 100, y + j * 100, 100, 100)
        tiles.append((n, result))
    shuffle(tiles)

def draw():
    mx, my = py5.mouse_x, py5.mouse_y
    for k, (i, j) in enumerate(product(range(7), repeat=2)):
        x, y = i * 100, j * 100
        n, t = tiles[k]
        py5.image(t, x, y)
        if py5.is_key_pressed:
            py5.text(n, 50 + x, 50 + y)
    for i, j in product(range(7), repeat=2):
        x, y = i * 100, j * 100
        if x < mx and x + 100 > mx and y < my and y + 100 > my:
            py5.no_fill()
            py5.stroke_weight(3)
            py5.rect(x, y, 100, 100)
                
def key_pressed():
    if py5.key == 's':
        py5.save_frame('####.png')
        start()
    
py5.run_sketch(block=False)
    