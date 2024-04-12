# Foto do Lobo: Carlos Delgado
# https://commons.wikimedia.org/wiki/File:Canis_lupus_signatus_-_01.jpg

def setup():
    global img
    size(800 , 800)  # tamanho da área de desenho
    img = load_image('lobo.jpg') # carregando imagem
    print(img.width, img.height)


def draw():
    global n
    n = mouse_x / 800
    image(img, 0, 0,
          img.width * 2,
          img.height * 2)
    apply_filter(THRESHOLD, n)    

def key_pressed():
    if key == 's':
        nome_arquivo = f'saida{nivel}.png'
        save(nome_arquivo)
        print(nome_arquivo)

def key_pressed():
    save(f'out{n}.jpg')
    