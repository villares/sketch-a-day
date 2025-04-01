tamanho = 10

def setup():
    global img
    size(600, 600)
    img = load_image('a.png')
    no_stroke()
    #image(img, 0, 0, 400, 400)   # image(x, y, w, h)
    #image(img, 0, 0, 400, 200)    
    #image(img, 0, 0, img.width * 0.3, img.height * 0.3)

def draw():
    background(0)
    colunas = int(width / tamanho)
    filas = int(height / tamanho)
    escala = 1
    offset_x, offset_y = 0, 0 #mouse_x, mouse_y
    print(mouse_x, mouse_y)
    for coluna in range(colunas):
        for fila in range(filas):
            x = int(coluna * tamanho * escala + offset_x * escala)
            y = int(fila * tamanho * escala + offset_y * escala)
            cor = img.get_pixels(x, y)
            matiz = hue(cor)
            bri = brightness(cor) # 0 a 255
            color_mode(HSB) # matiz, sat, bri                        
            nova_cor = color((matiz + 64) % 255, 255, bri)
            fill(nova_cor)
            d = bri / 255 * tamanho
            circle(x / escala - offset_x,
                   y / escala - offset_y, d)
    
def key_pressed():
    global tamanho
    if key == 'a':
        tamanho = tamanho + 1
    if key == 'z' and tamanho > 1:
        tamanho = tamanho - 1
