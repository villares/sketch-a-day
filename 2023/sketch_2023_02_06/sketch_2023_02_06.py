
imagens = []
h = 100  # altura do espaço para cada imagem
margin = 5
starting = 0

def setup():
    global colunas, linhas
    size(1400, 700)

def draw():
    global fila
    background(0)
    x = y = fila = 0
    for i, (nome, img) in enumerate(imagens[starting:]):
        fator = h / img.height
        if x + img.width * fator + margin> width:
            x = 0
            fila = i if fila == 0 else fila
            y += h + margin
        if y + img.height * fator + margin> height:
            print(1)
            break
        image(img, x, y, img.width * fator, img.height * fator)
        x += img.width * fator + margin
        
                
    if not imagens:   # if len(imagens) == 0:
        text_size(20)
        text("aperte 'o' para selecionar uma pasta\n"  # note ausência da vírgula aqui
             "aperte a barra de espaço para limpar a grade",
             100, 100)

def key_pressed():
    global starting, h
    if key == 'o':
        select_folder("Selecione uma pasta", adicionar_imagens)
        #adicionar_imagens('/home/villares/Imagens/')
    elif key == ' ':
        imagens[:] = []  # esvazia a lista de imagens
    elif key == 'p':
        save_frame('####.png')
    elif key == '=':
        starting += fila
    elif key == '-' and starting - fila > 0:
        starting -= fila
    elif key == 'a':
        h += margin
    elif key == 'z' and h > margin:
        h -= margin


def adicionar_imagens(dir_path):
    if dir_path == None:
        print("Seleção cancelada.")
    else:
        print("Pasta selecionada: " + dir_path)
        for file_path in lista_imagens(dir_path):
            img = load_image(file_path)
            print(f'imagem {file_path.name} carregada.')
            imagens.append((file_path.name, img))
        print(f'Número de imagens: {len(imagens)}')

def lista_imagens(data_path):
    """
    Devolve uma a lista dos caminhos (objetos pathlib.Path) dos arquivos
    de imagem contidos na pasta `data_path`
    """
    # extensões dos formatos de imagem que o Processing aceita!
    valid_ext = ('jpg', 'png', 'jpeg', 'gif', 'tif', 'tga')
    data_path = Path(data_path) # Garante objeto pathlib.Path
    try:
        f_list = [item for item in data_path.rglob('*')
                  if item.is_file() and item.suffix.lower()[1:] in valid_ext]
    except Exception as e:
        print(e)
        return []
    return f_list
