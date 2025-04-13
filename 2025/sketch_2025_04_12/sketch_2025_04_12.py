import py5

url = 'https://upload.wikimedia.org/wikipedia/commons/c/cb/Mapa_de_S%C3%A3o_Paulo_-_1924.jpg'
S = 90

def setup():
    global img, fonts
    py5.size(800, 800)
    img = py5.load_image(url)
    # Get Tomorrow from 
    fonts = [py5.create_font(name, S)
             for name in py5.Py5Font.list()
             if 'Tomorrow' in name]     
    py5.no_loop()

def draw():
    x = py5.random_int(img.width - py5.width)
    y = py5.random_int(img.height - py5.height)
#    result = py5.create_image(py5.width, py5.height, py5.RGB)
#    result.copy(img, x, y, py5.width, py5.height, 0, 0, py5.width, py5.height)
    result = img.get_pixels(x, y, py5.width, py5.height)
    py5.image(result, 0, 0)
    py5.text_font(py5.random_choice(fonts))
    py5.text_align(py5.LEFT, py5.TOP)
    py5.text_leading(S * 0.9)
    py5.text('São Paulo\nontem ou\namanhã,\nnunca hoje', 50, 50)
                
def key_pressed():
    py5.save_frame('####.png')
    py5.redraw()
    
py5.run_sketch(block=False)
    