from itertools import product
import py5

url = 'https://upload.wikimedia.org/wikipedia/commons/c/cb/Mapa_de_S%C3%A3o_Paulo_-_1924.jpg'
S = 24

def setup():
    global img, fonts
    py5.size(700, 700)
    img = py5.load_image(url)
    # Get Tomorrow from 
    fonts = [py5.create_font(name, S)
             for name in py5.Py5Font.list()
             if 'Tomorrow Bold' in name]     
    py5.no_loop()

def draw():
    for k, (i, j) in enumerate(product(range(7), repeat=2), 1):
        x = py5.random_int(img.width - py5.width)
        y = py5.random_int(img.height - py5.height)
        result = img.get_pixels(x, y, 100, 100)
        py5.image(result, i * 100, j * 100)
        py5.text_font(py5.random_choice(fonts))
        py5.text_align(py5.CENTER, py5.CENTER)
        py5.text(k, 50 + i * 100, 50 + j * 100)
                
def key_pressed():
    py5.save_frame('####.png')
    py5.redraw()
    
py5.run_sketch(block=False)
    