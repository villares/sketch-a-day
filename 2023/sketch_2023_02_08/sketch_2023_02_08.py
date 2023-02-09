from PIL import Image

imagens = []
starting_h = h = 75  # altura do espaço para cada imagem
margin = 5
starting = 0


def setup():
    global colunas, linhas
    size(1400, 700)

def draw():
    global x, y
    background(0)
    x = y = 0
    draw_images(imagens, h)
    if not imagens:   # if len(imagens) == 0:
        text_size(20)
        text("aperte 'o' para selecionar uma pasta\n"  # note ausência da vírgula aqui
             "aperte a barra de espaço para limpar a grade",
             100, 100)    
    
def draw_images(imgs, h):
    for i, el in enumerate(imgs):
        if isinstance(el, tuple):
           draw_image_el(el, h)
        elif isinstance(el, list):
           draw_images(el, h - margin) 

def draw_image_el(el, h):
    global x, y
    nome, img, path, screen = el
    f = h / starting_h
    if x + img.width * f + margin > width:
        x = 0
        y += h + margin
    if y + img.height + margin> height:
        return # does not draw or update image
    image(img, x, y, img.width * f, img.height * f)
    screen[:] = (x, y, img.width * f, img.height * f) 
    x += img.width * f + margin
    
        
                


# def mouse_pressed():
#     for name, _, _, (x, y, w, h) in imagens:
#         if x < mouse_x < x + w and y < mouse_y < y + h:
#             print(name)

def key_pressed():
    global starting, h
    if key == 'o':
        select_folder("Selecione uma pasta", adicionar_imagens)
        #adicionar_imagens('/home/villares/Imagens/')
    elif key == ' ':
        imagens[:] = []  # esvazia a lista de imagens
    elif key == 'p':
        save_frame('####.png')
    elif key == '=' and starting < len(imagens) - 10:
        starting += 10
    elif key == '-' and starting - 10 > 0:
        starting -= 10
    elif key == 'a':
        h += margin
    elif key == 'z' and h > margin:
        h -= margin


def adicionar_imagens(dir_path):
    if dir_path == None:
        print("Seleção cancelada.")
    else:
        print("Pasta selecionada: " + dir_path)
        imagens[:] = lista_imagens_recursiva(Path(dir_path))
        print(f'Número de imagens: {len(imagens)}')

def lista_imagens_recursiva(path):
    valid_ext = ('jpg', 'png', 'jpeg', 'gif', 'tif', 'tga')
    result = []
    for item in path.iterdir():
        if item.is_file() and item.suffix.lower()[1:] in valid_ext:
            try:
                full_img = Image.open(item)
                iw, ih = full_img.size
                fator = h / ih
                img = convert_image(full_img.resize((int(iw * fator), h)))
                del full_img
                print(f'imagem {item} carregada.')
                result.append((item.name, img, item, [0, 0, 0, 0]))
            except Exception as e:
                print(item.name, item)
                print(e)
        elif item.is_dir():
            if sub := lista_imagens_recursiva(item):
                result.append(sub)
    return result


