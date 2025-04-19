
url = 'https://upload.wikimedia.org/wikipedia/commons/c/cb/Mapa_de_S%C3%A3o_Paulo_-_1924.jpg'

def setup():
    global img, mascara
    size(500, 500)
    img = load_image(url)
    mascara = mascara_hexagonal(400, 400)
    no_loop()

def draw():
    background(100)
    x = random_int(200, img.width - 200)
    y = random_int(200, img.height - 200)
    recorte = recorte_com_mascara(img, mascara, x, y)
    image_mode(CENTER)
    image(recorte, 250, 250)          
    save('recorte_hexagonal.png')
    
def mascara_hexagonal(w, h):
    m = create_graphics(int(w), int(h))
    m.begin_draw()
    m.fill(255)
    m.no_stroke()
    with m.begin_shape():
        for n in range(6):
            ang = (n + 0.5) * TWO_PI / 6 
            x = w / 2 * cos(ang) + w / 2
            y = h / 2 * sin(ang) + h / 2
            m.vertex(x, y)
    m.end_draw()
    return m
         
def recorte_com_mascara(img, mascara, x, y):    
    w, h = mascara.width, mascara.height
    resultado = create_image(mascara.width, mascara.height, ARGB)
    resultado.copy(img, int(x), int(y), w, h, 0, 0, w, h)
    resultado.mask(mascara)
    return resultado

def key_pressed():
    redraw()
