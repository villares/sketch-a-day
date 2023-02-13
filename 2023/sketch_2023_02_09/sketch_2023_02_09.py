from PIL import Image

imagens = []
starting_h = h = 75  # altura do espaço para cada imagem
margin = 5
starting = 0


def setup():
    size(1400, 700)

def draw():
    global x, y
    background(0)
    x = y = 0
    #draw_images(imagens, h)
    draw_records(0, 0, width, height, imagens)
    if not imagens:   # if len(imagens) == 0:
        text_size(20)
        text("aperte 'o' para selecionar uma pasta\n"  # note ausência da vírgula aqui
             "aperte a barra de espaço para limpar a grade",
             100, 100)    
  
  
  
def draw_records(xo, yo, wo, ho, records, **kwargs):
    margin = kwargs.pop('margin', 5)
    x, y = xo + margin, yo + margin,
    w, h = wo - 2 * margin, ho - 2 * margin
    if isinstance(records, list):
        n = int(sqrt(len(records))) 
        i = 0
        for j in range(n):
            ww = w / n
            for k in range(n):
                hh = h / n
                if i < len(records):
                    draw_records(x + j * ww, y + k * hh, ww, hh, records[i])
                    i += 1
    elif isinstance(records, tuple):
        nome, img, path, screen = records
        image(img, x, y, w, h)
        
#     rx = ry = 0
#     for i, (name, area, sub) in enumerate(records):
#         hue = remap(area, 0, total_area / 4, 60, 300)
#         bri = remap(area, 0, total_area / 4, 100, 50)
#         if w > h:
#             rw, rh = remap(area, 0, total_area, 0, w), h
#         else:
#             rw, rh = w, remap(area, 0, total_area, 0, h)
#         rect(x + rx, y + ry, abs(rw), abs(rh), fill=f"hsl({hue},80%,{bri}%)")
#         if sub:
#             if rw * rh > 20000 and rh >= margin * 3 and rw >= margin * 3:
#                 next_sub = choice((1, 0))
#             else:
#                 next_sub = 0
#             next_records = generate_records(name, next_sub)
#             draw_records(x + rx, y + ry, rw, rh, next_records)
#         else:
#             ts = 5
#             while len(name) * ts < rw and ts < rh / 3:
#                 ts += 1
#             if ts != 5:
#                 text(x + rx + rw / 2,
#                      y + ry + rh / 2 + ts / 2,
#                      name, ts, fill='black')
#             else:
#                 circle(x + rx + rw / 2, y + ry + rh / 2, min(rh, rw) / 10, fill='black')
#         if w > h:
#             rx += rw
#         else:
#             ry += rh
  
  
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


