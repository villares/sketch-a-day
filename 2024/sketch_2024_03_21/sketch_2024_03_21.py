# imagem: https://commons.wikimedia.org/wiki/Category:Kittens#/media/File:Six_weeks_old_cat_(aka).jpg


tamanho = 10  # global

def setup():
    global img, ar
    size(960, 640)
    #no_smooth()
    img = load_image('imagem.jpg')        
    ar = img.width / img.height
    print(img.width, img.height, ar)
        
def draw():
    no_stroke()
    background(255)
    colunas = int(width / tamanho)
    filas = int(height / tamanho) 
    for num_fila in range(filas):
        y = tamanho / 2 + tamanho * num_fila
        for num_col in range(colunas):  # num_col 0, 1, 2 ... 19
            x = tamanho / 2 + tamanho * num_col
            cor = conta_gotas(x, y, img)
            fill(cor)
#             m = hue(cor)
            b = brightness(cor) # 0 ... 255
#             #d = tamanho / 255 * b
            d = remap(b, 0, 255, tamanho, 0)
#             color_mode(HSB) # matiz, sat, brilho
#             fill(m, 255, 128)
            ellipse(x, y, d,
                    tamanho / 2 + tamanho / 2 * sin(dist(x, y, 400, 400) / 20 + frame_count / 20))   

def conta_gotas(x, y, img_source):
    xi = int(remap(x, 0, width, 0, img_source.width))
    yi = int(remap(y, 0, height, 0, img_source.height))
    return img_source.get_pixels(xi, yi)
    
def key_pressed():
    global tamanho
    if key == '-' and tamanho > 1:
        tamanho = tamanho - 1
    elif key == '+' or key == '=':
        tamanho = tamanho + 1
    elif key == 's':
        save_frame('####.png')
        